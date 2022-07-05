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

from scrape.scrapeProductList import scrapeProductList


from datetime import date, datetime
import pandas as pd
pd.set_option("display.max_columns", None)


def main():

    config = {
        'shop': "05-001",
        'url': "https://p-bandai.com/hk/search?text=&sort=relevance&shop={}&page={}",
        'scraped_file_folder': "./product_list/",
    }

    productListScrapper = scrapeProductList(url=config.get("url"),
                                               shop=config.get("shop"),
                                               scraped_file_folder=config.get("scraped_file_folder"))
    productListScrapper.scrapeAllPageData()
    df_result = productListScrapper.getAllPageData()

    print(df_result.shape)
    print(df_result.head(3))
    print(df_result.tail(3))


if __name__ == "__main__":
    main()
