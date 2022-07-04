

from datetime import datetime
import os
from typing import Union
from bs4 import BeautifulSoup

import pandas as pd


class commonHelper():

    def __init__(self):
        pass

    def saveFile(self, data: Union[pd.DataFrame, BeautifulSoup],
                shop: str,
                folder: str,
                filename: str,
                data_type: str = 'csv',
                ):
        yyyymmdd = datetime.now().strftime('%Y%m%d')
        path = f"{folder}/{data_type}/shop={shop}/dt={yyyymmdd}/"
        filename = f"{filename}_{yyyymmdd}.{data_type}"
        save_path = f"{path}/{filename}"
        self.checkFolderPath(path)
        
        {
            # immediately invoked function
            "csv": lambda f: data.to_csv(save_path, index=False),
            "html": lambda f: open(save_path, mode='wt', encoding='utf-8').write(str(data)),
        }.get(data_type)('')


    def checkFolderPath(self, folder_path: str):
        # Create a new directory because it does not exist 
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(">>> Created folder: {}".format(folder_path))
