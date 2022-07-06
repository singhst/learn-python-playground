from typing import List, Union
from scrape.helper import commonHelper

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option("display.max_columns", None)


class scrapeProductList(commonHelper):

    def __init__(self,
                 url_pattern: str,
                 shop: str,
                 scraped_file_folder: str="",
                 ) -> None:
        self.url_pattern = url_pattern
        self.shop = shop
        self.scraped_file_folder = scraped_file_folder

        self._page_number = 0
        self.data_list: List[dict] = []     #: List[pd.Dataframe] = []


    def scrapeOnePageData(self,
                          url: str
                          ) -> List[dict]:  #pd.DataFrame:
        """Gets table data from the web. Return the extracted table as `pandas` `dataframe`.

        Parameters
        ----------
        url : str
            The url of the website, e.g. `https://reelgood.com/movies?offset=50`
        class_of_table : str

        Returns
        -------
        `list of dict`
        """

        # add User-Agent to header to pretend as browser visit, more detials can be found in FireBug plugin
        # if we don't add the below, error message occurs. ERROR: urllib.error.HTTPError: HTTP Error 403: Forbidden
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url=url, headers=headers)

        returned_html = urllib.request.urlopen(req).read()
        soup_object = BeautifulSoup(returned_html, 'html.parser')
        products = soup_object.find_all("div", {"class": "col-xs-6 col-sm-6 col-md-4 col-lg-3"})
        # print(type(products))

        filename = "shop={}_page={}".format(self.shop, self._page_number)
        self.saveFile(data=products, 
                folder=self.scraped_file_folder, 
                shop=self.shop,
                filename=filename, 
                data_type="html")

        data = []
        for product in products:
            result = {
                "page"              : self._page_number,
                "name"              : product.find("img", {"class": "img-responsive"}).get("alt"),
                "shop_product_code" : product.find("a", {"class": "m-card m-card--lg js-hover"}).get("href").replace("/hk/item/", ""),
                "img_url"           : product.find("img", {"class": "img-responsive"}).get("src"),
            }
            data.append(result)

        # sing> change back to return `list of dict`
        return data #pd.DataFrame(data)


    def scrapeAllPageData(self):
        # boolean to check `end of the page`
        # `True` : data presents in this page
        # `False`: no data presents in this page
        valid_page = True

        while valid_page:
            _whole_url = self.url_pattern.format(self.shop, self._page_number)
            print('>>> _whole_url:', _whole_url)

            # _df = self.scrapeOnePageData(_whole_url)
            # if _df.empty:
            #     valid_page = False

            # self.data_list.append(_df)

            _data = self.scrapeOnePageData(_whole_url)
            if len(_data) <= 0:
                valid_page = False

            self.data_list.extend(_data)

            self._page_number += 1

            if (self._page_number >= 2):
                break


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
