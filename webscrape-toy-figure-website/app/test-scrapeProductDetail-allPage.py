from pathlib import Path
from app.scrape.scrapeProductDetail import scrapeProductDetail

ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent
print(BASE_PATH)
print(ROOT)

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

    s.saveInCsv()

    s.saveInDb(new_details=[
        {"name": 'xxx', "shop_product_code": "N2623282001001", "img_url": "yyyy"},
        {"name": 'xxx', "shop_product_code": "11111",
         "img_url": "yyyy"}
    ])
