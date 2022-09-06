import { promises as fsPromises, PathLike } from "fs";

const asyncReadFile = async (filename: PathLike | fsPromises.FileHandle) => {
  try {
    const contents = await fsPromises.readFile(filename, "utf-8");

    const arr = contents.split("\n");

    // console.log(arr); // 👉️ ['One', 'Two', 'Three', 'Four']

    return arr;
  } catch (err) {
    console.log(err);
  }
}

const readJsonToObjArray = async () => {
  let json_array: Array<JSON> = [];
  const return_array =
    (await asyncReadFile(
      "./webscrape-toy-figure-website/product_detail/product_detail.json"
    )) ?? [];
  return_array.forEach(async (element) => {
    try {
      console.log(`element (${typeof element}): ${element}`);
      if (element !== "" && element !== null) {
        json_array.push(JSON.parse(element));
      }
    } catch (error) {
      console.log(error);
    }
  });
  console.log(`json_array: ${JSON.stringify(json_array)}`);
  return json_array;
}

readJsonToObjArray();
