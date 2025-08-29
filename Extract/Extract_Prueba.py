import pandas as pd
from Config.Config_Prueba import Config

class Extract:
    @staticmethod
    def extract_data(file_path):

        print(f"Extrayendo datos desde {file_path}...")

        data = pd.read_csv(file_path)
        
        
        return data
