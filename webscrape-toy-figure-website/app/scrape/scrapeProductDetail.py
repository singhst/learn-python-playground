from typing import List, Union
from urllib.error import HTTPError, URLError
from scrape.helper import commonHelper
from scrape import helper

import re
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
pd.set_option("display.max_columns", None)


class scrapeProductDetail(commonHelper):

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

        print(">>> __init__(), kwargs=",kwargs)
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

            product__schedule: dict = {
                "????????????": None,
                "????????????": None,
                "????????????": None,
                "??????": None,
            }
            for m_schedule in product__description.find_all("div", {"class": "m-schedule"}):
                _class = m_schedule.find("p", {"class": "m-schedule__th"}).string
                regex = re.compile(r'[\n\r\t]') #remove special characters
                _class = regex.sub("", _class)
                product__schedule[_class] = m_schedule.find("p", {"class": "m-schedule__td"}).string
            print(">>> product__schedule=", product__schedule)

            result = {
                "shop_product_code" : shop_product_code,
                "name"              : kwargs.get("name") if kwargs.get("name") else product__description.find("h1", {"class": "o-product__name"}).string,
                "currency"          : product__description.find("span", {"class": "o-product__currency"}).string,
                "price"             : product__description.find("span", {"class": "o-product__price"}).string,
                "delivery_date"     : datetime.strptime(product__schedule.get("????????????"), "%Y. %m"),
                "order_time_start"  : datetime.strptime(product__schedule.get("????????????"), "%Y. %m.%d %H:%M"),
                # "order_time_end"    : datetime.strptime(product__schedule.get("????????????"), "%Y. %m.%d %H:%M"),
                "company"           : product__schedule.get("??????"),
                "order_status"      : False if "disabled" in product__description.find("button", {"id": "addToCartButton"}) else True,
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

            _data = self.scrapeOnePageData(url=_whole_url, **_exist_product)
            self.data_list.append(_data)


    def getAllPageData(self, return_type: str = 'dict_list') -> Union[List[dict], pd.DataFrame]:
        '''
        `return_type`: `str`, "dict_list" or "dataframe"
        '''

        _df = pd.DataFrame(self.data_list)
        filename = f"shop={self.shop}"
        self.saveFile(data=_df,
                      shop=self.shop,
                      folder=self.scraped_file_folder,
                      filename=filename,
                      data_type="csv")

        return_data = {
            'dict_list': self.data_list,
            'dataframe': _df,
        }
        return return_data[return_type]
