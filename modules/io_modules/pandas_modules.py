import pandas as pd
import os
class CsvModules():
    @staticmethod
    def read_csv(path):
        if not os.path.exists(path):
            raise Exception("File not found")
        return pd.read_csv(path)