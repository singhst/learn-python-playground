// ==================================================================
//
// https://stackabuse.com/executing-shell-commands-with-node-js/
//
// ==================================================================

import { exec } from "child_process";

exec("ls -la", (error, stdout, stderr) => {
  if (error) {
    console.log(`error: ${error.message}`);
    return;
  }
  if (stderr) {
    console.log(`stderr: ${stderr}`);
    return;
  }
  console.log(`typeof stdout: ${typeof stdout}`);
  console.log(`stdout: ${stdout}`);
});
