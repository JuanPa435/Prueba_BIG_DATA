import pandas as pd

class Transform:
    @staticmethod
    def clean_data(data):
        print("Limpiando datos...")

        # Eliminar duplicados
        data = data.drop_duplicates()

        # Rellenar valores con la mediana
        numeric_cols = data.select_dtypes(include='number').columns
        for col in numeric_cols:
            median_value = data[col].median()
            data[col] = data[col].fillna(median_value) 

        # Rellenar valores con la moda
        categorical_cols = data.select_dtypes(include='object').columns
        for col in categorical_cols:
            mode_value = data[col].mode()[0] 
            data[col] = data[col].fillna(mode_value) 
        return data
