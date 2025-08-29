from Config.Config_Prueba import Config
from Extract.Extract_Prueba import Extract
from Load.Load_Prueba import Load
from Transform.Transform_Prueba import Transform

class DataCleaner:
    def __init__(self, config):
        self.config = config

    def execute(self):
        data = Extract.extract_data(self.config.INPUT_FILE)
        print("Primeros 5 registros del archivo original:")
        print(data.head()) 
        
        # Limpiar los datos
        cleaned_data = Transform.clean_data(data)
        
        # Guardar los datos limpios
        print(f"Guardando datos limpios en {self.config.OUTPUT_FILE}...")
        cleaned_data.to_csv(self.config.OUTPUT_FILE, index=False)

        print("Primeros 5 registros del archivo limpio:")
        print(cleaned_data.head())
        print("Limpieza completada.")

if __name__ == "__main__":
    config = Config()
    cleaner = DataCleaner(config)
    cleaner.execute()
