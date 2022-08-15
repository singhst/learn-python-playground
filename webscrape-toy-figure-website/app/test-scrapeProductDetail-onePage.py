from scrape.scrapeProductDetail import scrapeProductDetail

if __name__ == "__main__":
    s = scrapeProductDetail(url_pattern="https://p-bandai.com/hk/item/{shop_product_code}",
    shop='test',
    shop_product_codes="N2623282001001",
    scraped_file_folder="./product_list/",
    )
    
    print(s.scrapeOnePageData(shop_product_code="N2623282001001"))  #order_status: 預購已經結束
    print(s.scrapeOnePageData(shop_product_code="N2611062001001"))  #order_status: 缺貨
    print(s.scrapeOnePageData(shop_product_code="N2634941001001"))  #order_status: 送出訂單
    print(s.scrapeOnePageData(shop_product_code="xxx"))             #unknown product code
