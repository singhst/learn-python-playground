#!/usr/bin/env python

"""
routing pattern,

URL:
    https://p-bandai.com/hk
    /search?
    text=
    &sort=relevance
    &shop=05-<shop number>&page=<[1..9], shop number>
    &page=<page number>

example:
    https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=21
"""

from cgitb import html
import os
import sys
from datetime import date, datetime
from turtle import ht
from typing import List, Union
# import getopt
import urllib.request
from bs4 import BeautifulSoup
import selenium
import pandas as pd
pd.set_option("display.max_columns", None)


class webScrapeProductList:

    def __init__(self,
                 url: str,
                 shop: str,
                 scraped_file_folder: str="",
                 ) -> None:
        self.url_pattern = url
        self.shop = shop
        self.scraped_file_folder = scraped_file_folder

        self._page_number = 0
        self.df_list = []


    def scrapeOnePageData(self,
                          url: str
                          ) -> pd.DataFrame:
        """Gets table data from the web. Return the extracted table as `pandas` `dataframe`.

        Parameters
        ----------
        url : str
            The url of the website, e.g. `https://reelgood.com/movies?offset=50`
        class_of_table : str

        Returns
        -------
        pd.Dataframe
            `dataframe` of names of xxxxx.
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
        saveFile(data=products, 
                folder=self.scraped_file_folder, 
                shop=self.shop,
                filename=filename, 
                data_type="html")

        data = []
        for product in products:
            result = {
                "page"              : self._page_number,
                "name"              : product.find("img", {"class": "img-responsive"}).get("alt"),
                "shop_product_code" : product.find("a", {"class": "m-card m-card--lg js-hover"}).get("href"),
                "img_url"           : product.find("img", {"class": "img-responsive"}).get("src"),
            }
            data.append(result)

        return pd.DataFrame(data)


    def scrapeAllPageData(self):
        # boolean to check `end of the page`
        # `True` : data presents in this page
        # `False`: no data presents in this page
        valid_page = True

        while valid_page:
            _whole_url = self.url_pattern.format(self.shop, self._page_number)
            print('>>> _whole_url:', _whole_url)

            _df = self.scrapeOnePageData(_whole_url)
            self.df_list.append(_df)

            if _df.empty:
                valid_page = False

            self._page_number += 1
            # break


    def getAllPageData(self) -> pd.DataFrame:
        _df = pd.concat(self.df_list)
        filename = f"shop={self.shop}"
        saveFile(data=_df, 
                 shop=self.shop,
                 folder=self.scraped_file_folder,
                 filename=filename, 
                 data_type="csv")
        return _df


def saveFile(data: Union[pd.DataFrame, BeautifulSoup],
             shop: str,
             folder: str,
             filename: str,
             data_type: str = 'csv',
             ):
    yyyymmdd = datetime.now().strftime('%Y%m%d')
    path = f"{folder}/{data_type}/shop={shop}/dt={yyyymmdd}/"
    filename = f"{filename}_{yyyymmdd}.{data_type}"
    save_path = f"{path}/{filename}"
    checkFolderPath(path)
    
    {
        # immediately invoked function
        "csv": lambda f: data.to_csv(save_path, index=False),
        "html": lambda f: open(save_path, mode='wt', encoding='utf-8').write(str(data)),
    }.get(data_type)('')


def checkFolderPath(folder_path: str):
    # Create a new directory because it does not exist 
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(">>> Created folder: {}".format(folder_path))


def main():

    config = {
        'shop': "05-001",
        'url': "https://p-bandai.com/hk/search?text=&sort=relevance&shop={}&page={}",
        'scraped_file_folder': "./product_list/",
    }

    productListScrapper = webScrapeProductList(url=config.get("url"),
                                               shop=config.get("shop"),
                                               scraped_file_folder=config.get("scraped_file_folder"))
    productListScrapper.scrapeAllPageData()
    df_result = productListScrapper.getAllPageData()

    print(df_result.shape)
    print(df_result.head(3))
    print(df_result.tail(3))


if __name__ == "__main__":
    main()
