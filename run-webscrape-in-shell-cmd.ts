import { exec } from "child_process";

// [x] [ing] change path
const command = `cd \$\{HOME\}/Documents/GitHub/learn-python-playground/webscrape-toy-figure-website;
pwd;
. venv/bin/activate;
poetry run python app/main_webscrapping.py;
`;
console.log(`command:\n${command}`)

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
  console.log(`stdout: length=${stdout.length}, stdout=\n${stdout.slice(0,40000)}`);
});
