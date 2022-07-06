from scrape.scrapeProductDetail import scrapeProductDetail

if __name__ == "__main__":
    s = scrapeProductDetail(url_pattern="https://p-bandai.com/hk/item/{shop_product_code}",
                            shop='test',
                            # shop_product_codes="N2623282001001",
                            scraped_file_folder="./product_list/",
                            existing_product_list=[
                                    {"name": 'xxx', "shop_product_code": "N2623282001001", "img_url": "yyyy"},
                                    {"name": 'xxx', "shop_product_code": "11111", "img_url": "yyyy"}
                                    ]
                            )

    s.scrapeAllPageData()
    print(s.getAllPageData())