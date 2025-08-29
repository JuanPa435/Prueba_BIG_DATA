# Proyecto de Limpieza de Datos

## Descripción

Este proyecto permite cargar un archivo CSV, limpiarlo de registros duplicados y valores nulos, y luego guardar el archivo limpio en un nuevo archivo CSV. Además, durante el proceso, se imprime una muestra de los primeros 5 registros tanto del archivo original como del archivo limpio, para que puedas verificar los cambios realizados.

### Flujo de trabajo:
1. **Extracción**: Cargar datos desde un archivo CSV.
2. **Carga**: Almacenar los datos en un DataFrame de `pandas`.
3. **Transformación**: Limpiar los datos:
    - Eliminar duplicados.
    - Rellenar valores nulos en columnas numéricas con la mediana.
    - Rellenar valores nulos en columnas categóricas con la moda.
4. **Guardado**: Guardar los datos limpios en un nuevo archivo CSV.


