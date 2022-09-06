import { exec } from "child_process";
import fs from "fs";
import readline from "readline";


const json_folder = "./product_detail/";
const json_filename = "product_detail";
// [x] [ing] change path
const command = `cd \$\{HOME\}/Documents/GitHub/learn-python-playground/webscrape-toy-figure-website;
pwd;
. venv/bin/activate;
poetry run python app/main_webscrapping.py --full_path="${json_folder}" --full_filename="${json_filename}";
`;
console.log(`command:\n${command}`);

async function scrapeProductDetails() {
  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.log(`error: ${error.message}`);
      return;
    }
    if (stderr) {
      console.log(`stderr: ${stderr}`);
      return;
    }
    console.log(`typeof stdout: ${typeof stdout}`);
    console.log(`stdout: length=${stdout.length}, stdout=\n${stdout}`);
  });
}

async function main() {
  await scrapeProductDetails();
}

main();
