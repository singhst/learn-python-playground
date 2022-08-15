from typing import List, Union
from urllib.error import HTTPError, URLError
from app.models.product import Product
from app import deps
from app.scrape.helper import commonHelper
from app.scrape.helperDatabse import databseHelper

from sqlalchemy.orm import Session
import re
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
pd.set_option("display.max_columns", None)


class scrapeProductDetail(commonHelper, databseHelper):

    def __init__(self,
                 shop: str,
                #  shop_product_codes: Union[str, List[str]] = "",
                 url_pattern: str="https://p-bandai.com/hk/item/{shop_product_code}",
                 scraped_file_folder: str="",
                 **kwargs
                 ):
        '''
        `kwargs`: `{"existing_product_list": [{"name": xxx, "shop_product_code": xxx, "img_url": xxx}]}`
        '''
        self.url_pattern:str = url_pattern
        self.shop:str = shop
        # self.shop_product_codes: Union[str, List[str]] = [shop_product_codes] if isinstance(shop_product_codes, str) else shop_product_codes
        self.scraped_file_folder: str = scraped_file_folder

        print(">>> __init__(), kwargs.keys()=",kwargs.keys())
        self.existing_product_list: List[dict] = kwargs.get("existing_product_list") if {"existing_product_list"}.issubset(kwargs.keys()) else None
        # self.existing_product_list: List[dict] = kwargs if (kwargs.keys() >= set('shop_product_codes', 'img_url')) else None   # `a >= b`: (1) is `a` the superset of `b`? (2) is `b` the subset of `a`?

        self.data_list: List[dict] = []


    def scrapeOnePageData(self,
                          shop_product_code: str,
                          **kwargs
                          ) -> dict:
        '''
        `kwargs`: `{"url": xxx, "name": xxx, "img_url": xxx}`
        '''
        print(">>> scrapeOnePageData(), kwargs=", kwargs)

        url = kwargs.get("url") if kwargs.get("url") else self.url_pattern.format(shop_product_code=shop_product_code)
        shop_product_code = kwargs.get("url").split("/")[-1] if kwargs.get("url") else shop_product_code
        print(">>> url= {}; shop_product_code= {}".format(url, shop_product_code))
        
        # add User-Agent to header to pretend as browser visit, more detials can be found in FireBug plugin
        # if we don't add the below, error message occurs. ERROR: urllib.error.HTTPError: HTTP Error 403: Forbidden
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
        req = urllib.request.Request(url=url, headers=headers)

        try:
            returned_html = urllib.request.urlopen(req).read()
            soup_object = BeautifulSoup(returned_html, 'html.parser')
            product__description = soup_object.find_all("div", {"class": "o-product__description"})[0]
            print(type(product__description))

            # filename = "detail-shop_product_code={}".format(shop_product_code)
            # self.saveFile(data=soup_object,
            #               folder=self.scraped_file_folder,
            #               shop=self.shop,
            #               filename=filename,
            #               data_type="html")

            # just want to preview the values under "m-schedule__td" tag
            product__schedule: dict = {
                "配送月份": None,
                "開始預購": None,
                "截止預購": None,
                "公司": None,
            }
            for m_schedule in product__description.find_all("div", {"class": "m-schedule"}):
                _class = m_schedule.find("p", {"class": "m-schedule__th"}).string
                regex = re.compile(r'[\n\r\t]') #remove special characters
                _class = regex.sub("", _class)
                product__schedule[_class] = m_schedule.find("p", {"class": "m-schedule__td"}).string
            print(">>> product__schedule=", product__schedule)

            add_to_cart_button_status = product__description.find("button", {"id": "addToCartButton"}).get_text(",",strip=True)
            print(">>> add_to_cart_button_status=", add_to_cart_button_status, type(add_to_cart_button_status))
            order_status = add_to_cart_button_status.split(",")[0]
            print(">>> order_status=", order_status, type(order_status))

            result = {
                "shop_product_code" : shop_product_code,
                "name"              : kwargs.get("name") if kwargs.get("name") else product__description.find("h1", {"class": "o-product__name"}).string,
                "currency"          : product__description.find("span", {"class": "o-product__currency"}).string,
                "price"             : product__description.find("span", {"class": "o-product__price"}).string,
                "delivery_date"     : datetime.strptime(product__schedule.get("配送月份"), "%Y. %m"),
                "order_time_start"  : datetime.strptime(product__schedule.get("開始預購"), "%Y. %m.%d %H:%M"),
                # "order_time_end"    : datetime.strptime(product__schedule.get("截止預購"), "%Y. %m.%d %H:%M"),
                "company"           : product__schedule.get("公司"),
                "order_status"      : order_status,
                "is_favourite"      : False, ###>>> need think, look like we need login before scrapping this
                "img_url"           : kwargs.get("img_url") if kwargs.get("img_url") else soup_object.find("meta", {"property": "og:image"}).get("content"),
                "scraped_time"      : datetime.now(),
            }

        except HTTPError as error:
            if error.code == 404:
                print("The server exists but the endpoint does not!")
                result = {
                    "shop_product_code" : shop_product_code,
                    "name"              : kwargs.get("name") if kwargs.get("name") else None,
                    "currency"          : None,
                    "price"             : None,
                    "delivery_date"     : None,
                    "order_time_start"  : None,
                    "order_time_end"    : None,
                    "company"           : None,
                    "order_status"      : None,
                    "is_favourite"      : None,
                    "img_url"           : kwargs.get("img_url") if kwargs.get("img_url") else None,
                    "scraped_time"      : datetime.now(),
                }
            else:
                print("The server exists but there was an Internal Error!")
        except URLError as error:
            print("The server does not exist!")

        return result


    def scrapeAllPageData(self):

        for _exist_product in self.existing_product_list:
            
            _whole_url = self.url_pattern.format(shop_product_code=_exist_product.get("shop_product_code"))
            print('>>> _whole_url:', _whole_url)

            result = self.scrapeOnePageData(url=_whole_url, **_exist_product)
            self.data_list.append(result)


    def getAllPageData(self, return_type: str = 'dict_list') -> Union[List[dict], pd.DataFrame]:
        '''
        `return_type`: `str`, "dict_list" or "dataframe"
        '''
        return_data = {
            'dict_list': self.data_list,
            'dataframe': pd.DataFrame(self.data_list),
        }
        return return_data[return_type]

    def saveInCsv(self):
        self._saveFile(data=pd.DataFrame(self.data_list),
                       shop=self.shop,
                       folder=self.scraped_file_folder,
                       filename=f"shop={self.shop}",
                       data_type="csv")

    def saveInJson(self):
        self._saveFile(data=pd.DataFrame(self.data_list),
                       shop=self.shop,
                       folder=self.scraped_file_folder,
                       filename=f"shop={self.shop}",
                       data_type="json")


    def saveInDb(self, db: Session=next(deps.get_db()), new_details: List[dict] = []):
        def checkDbTable():
            from sqlalchemy import inspect
            _engine = db.get_bind()
            inspector = inspect(_engine)
            schemas = inspector.get_schema_names()
            for schema in schemas:
                print("schema: %s" % schema)
                for table_name in inspector.get_table_names(schema=schema):
                    for column in inspector.get_columns(table_name, schema=schema):
                        print("Column: %s" % column)

        ### testing
        # checkDbTable()

        ### Outside data
        new_details = self.data_list if len(new_details) == 0 else new_details

        ### Get all data in the DB
        old_details = db.query(Product).all()
        
        _update: List = []
        _insert: List = []

        if len(old_details) == 0:
            ### If NO records exist in db, all new records need insert
            self.bulkInsert(db=db, db_table_data_model=Product, data_in=new_details)
        else:
            ### If some records already exist in db
            # 1. Existed records        ==> update this record
            # 2. Totally new records    ==> insert
            _max_id = max([_.id for _ in old_details])

            # split new records into (1) update (2) insert
            for _new_detail in new_details:
                _existed_detail = list(filter(lambda _old_detail: _old_detail.shop_product_code == _new_detail["shop_product_code"], old_details))
                _existed_detail = _existed_detail[0] if len(_existed_detail) > 0 else None
                if _existed_detail is not None:
                    _update.append({**_new_detail, "id":_existed_detail.id})
                else:
                    _max_id += 1
                    _insert.append({**_new_detail, "id":_max_id})

            print(">>> len(_update)={}, _update={}".format(len(_update), _update[:3]))
            print(">>> len(_insert)={}, _insert={}".format(len(_insert), _insert[:3]))

            self.bulkInsert(db=db, db_table_data_model=Product, data_in=_insert)
            self.bulkUpdate(db=db, db_table_data_model=Product, data_in=_update)
