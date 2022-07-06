from scrape.scrapeProductDetail import scrapeProductDetail

if __name__ == "__main__":
    s = scrapeProductDetail(url_pattern="https://p-bandai.com/hk/item/{shop_product_code}",
    shop='test',
    shop_product_codes="N2623282001001",
    scraped_file_folder="./product_list/",
    )
    
    print(s.scrapeOnePageData(shop_product_code="N2623282001001"))
    print(s.scrapeOnePageData(shop_product_code="xxx"))
