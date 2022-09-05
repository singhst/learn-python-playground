// =============================================================================================
//
// https://stackoverflow.com/a/60642845
//
// =============================================================================================

import fs from "fs";
import readline from "readline";

async function read_file() {
  const filePath =
    "./webscrape-toy-figure-website/product_detail/json/shop=05-001/dt=20220905/shop=05-001_20220905.json";
  var readData: Array<string> = [];

  let data = await new Promise((resolve, reject) => {
    try {
      readline
        .createInterface({
          input: fs.createReadStream(filePath),
          terminal: false,
        })
        .on("line", function (line) {
          console.log(typeof line)
          console.log(line)
          readData.push(JSON.parse(line));
        })
        .on("close", function () {
          resolve(readData);
        });
    } catch (e) {
      reject(e);
    }
  });

  console.log(data);
}

read_file();


// Output:
`
[
  {
    shop_product_code: 'N2641782001001',
    name: 'S.H.Figuarts TECTOR GEAR ZERO',
    currency: 'HK$',
    price: '490.00',
    delivery_date: 1675209600000,
    order_time_start: 1662390000000,
    company: 'BANDAI NAMCO ASIA CO., LTD.',
    order_status: '送出訂單',
    is_favourite: false,
    img_url: 'https://p-bandai.com/img/hk/p/t/N2641782001001_001.jpg',
    scraped_time: 1662398457205
  },
  {
    shop_product_code: 'N2641781001001',
    name: 'S.H.Figuarts GLITTER TRIGGER ETERNITY',
    currency: 'HK$',
    price: '440.00',
    delivery_date: 1672531200000,
    order_time_start: 1662202800000,
    company: 'BANDAI NAMCO ASIA CO., LTD.',
    order_status: '送出訂單',
    is_favourite: false,
    img_url: 'https://p-bandai.com/img/hk/p/t/N2641781001001_001.jpg',
    scraped_time: 1662398457417
  },
  ...
  ...
  ...
  {
    shop_product_code: 'N2606409001001',
    name: 'METAL ROBOT SPIRITS (Ka signature)＜SIDE MS＞HYAKU SHIKI KAI MASS PRODUCTION TYPE',
    currency: 'HK$',
    price: '1,140.00',
    delivery_date: 1654041600000,
    order_time_start: 1643382000000,
    company: 'BANDAI NAMCO ASIA CO., LTD.',
    order_status: '預購已經結束',
    is_favourite: false,
    img_url: 'https://p-bandai.com/img/hk/p/t/N2606409001001_001.jpg',
    scraped_time: 1662398476569
  }
]
`