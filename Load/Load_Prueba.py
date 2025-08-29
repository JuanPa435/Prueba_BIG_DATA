import pandas as pd
from Config.Config_Prueba import Config

class Load:
    @staticmethod
    def load_data(file_path):
        print(f"Cargando datos desde {file_path}...")
        return pd.read_csv(file_path)
