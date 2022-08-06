#!/usr/bin/env python

"""
routing pattern,

# (1) Product List
    URL:
        https://p-bandai.com
        /hk/search?
        text=
        &sort=relevance
        &shop=05-<shop number>&page=<[1..9], shop number>
        &page=<page number>

    example:
        https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=21

# (2) Product Detail
    URL:
        https://p-bandai.com
        /hk/item/<shop product code>

    example:
        https://p-bandai.com/hk/item/N2623282001001
"""
from pathlib import Path

from app.scrape.scrapeProductList import scrapeProductList
from app.scrape.scrapeProductDetail import scrapeProductDetail

import pandas as pd
pd.set_option("display.max_columns", None)


# Project Directories
ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent
print(BASE_PATH)
print(ROOT)

def main():

    config = {
        'shop': "05-001",
        # 'url': "https://p-bandai.com/hk/search?text=&sort=relevance&shop={}&page={}",
        'domain': "https://p-bandai.com",
        'product_list_slug': "/hk/search?text=&sort=relevance&shop={}&page={}",
        'product_detail_slug': "/hk/item/{shop_product_code}",
        'scraped_product_list_file_folder': "./product_list/",
        'scraped_product_detail_file_folder': "./product_detail/",
    }
    config['product_list_url'] = config.get('domain') + config.get('product_list_slug')
    config['product_detail_url'] = config.get('domain') + config.get('product_detail_slug')
    print('>>> config=', config)


    ## (1) Product list
    listScrapper = scrapeProductList(url_pattern=config.get("product_list_url"),
                                     shop=config.get("shop"),
                                     scraped_file_folder=config.get("scraped_product_list_file_folder"),
                                     max_page_number=2, #comment `max_page_number` to scrape 1000 pages
                                     )
    listScrapper.scrapeAllPageData()
    listScrapper.saveInCsv()
    _product_list = listScrapper.getAllPageData(return_type='dict_list')

    print(len(_product_list), len(_product_list[0].keys()))
    print(_product_list[:3])
    print()
    print(_product_list[-3:])

    # shop_product_codes = [_['shop_product_code'] for _ in _results]
    # print(shop_product_codes[:3])


    ### (2) Each product detail
    detailScrapper = scrapeProductDetail(url_pattern="https://p-bandai.com/hk/item/{shop_product_code}",
                                         shop=config.get("shop"),
                                         scraped_file_folder=config.get("scraped_product_detail_file_folder"),
                                         existing_product_list=_product_list
                                         )

    detailScrapper.scrapeAllPageData()
    detailScrapper.saveInCsv()
    detailScrapper.saveInDb()
    _product_details = detailScrapper.getAllPageData(return_type='dict_list')

    print(len(_product_details), len(_product_details[0].keys()))
    print(_product_details[:3])
    print()
    print(_product_details[-3:])


if __name__ == "__main__":
    main()
