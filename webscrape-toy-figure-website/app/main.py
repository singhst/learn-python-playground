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

from scrape.scrapeProductList import scrapeProductList

import pandas as pd
pd.set_option("display.max_columns", None)


def main():

    config = {
        'shop': "05-001",
        # 'url': "https://p-bandai.com/hk/search?text=&sort=relevance&shop={}&page={}",
        'domain': "https://p-bandai.com",
        'product_list_slug': "/hk/search?text=&sort=relevance&shop={}&page={}",
        'product_detail_slug': "/hk/item/{shop_product_code}",
        'scraped_file_folder': "./product_list/",
    }
    config['product_list_url'] = config.get('domain') + config.get('product_list_slug')
    config['product_detail_url'] = config.get('domain') + config.get('product_detail_slug')
    print('>>> config=', config)


    ## (1) Product list
    productListScrapper = scrapeProductList(url=config.get("product_list_url"),
                                            shop=config.get("shop"),
                                            scraped_file_folder=config.get("scraped_file_folder"))
    productListScrapper.scrapeAllPageData()

    _results = productListScrapper.getAllPageData(return_type='dict_list')

    print(len(_results), len(_results[0].keys()))
    print(_results[:3])
    print()
    print(_results[-3:])

    shop_product_codes = [_['shop_product_code'] for _ in _results]
    print(shop_product_codes[:3])


    ### (2) Each product detail
    # for _code in shop_product_codes:
        # ... scrape each product code's detail ...
        


if __name__ == "__main__":
    main()
