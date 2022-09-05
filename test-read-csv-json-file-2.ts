// =============================================================================================
//
// https://levelup.gitconnected.com/how-to-read-a-file-line-by-line-in-javascript-48d9a688fe49
//
// =============================================================================================

console.time('Time');
import fs from 'fs';
import readline from 'readline';

void (async () => {
  const rl = readline.createInterface({
    input: fs.createReadStream("./webscrape-toy-figure-website/product_detail/json/shop=05-001/dt=20220905/shop=05-001_20220905.json"),
    crlfDelay: Infinity,
  });

  let json_data = [];
  rl.on('line', (line: any) => {
    // console.log('line: ', JSON.parse(line));
  });

  console.log(json_data.length)
  console.log(json_data)

  await new Promise((res) => rl.once('close', res));

  console.log(`Used ${process.memoryUsage().heapUsed / 1024 / 1024} MB`);
  console.timeEnd('Time');
})();
