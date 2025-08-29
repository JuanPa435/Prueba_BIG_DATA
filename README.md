# Proyecto de Limpieza de Datos

Este proyecto tiene como objetivo extraer, limpiar y guardar datos provenientes de un archivo CSV. A través de una estructura modularizada, se utiliza un pipeline de extracción, carga, transformación y limpieza de los datos, todo ello siguiendo una organización de código limpia y escalable.

## Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas y archivos:

├── Config
│ ├── init.py
│ └── Config_Prueba.py # Configuraciones de rutas de archivos
├── Extract
│ ├── init.py
│ ├── Datos_Restaurant.csv # Archivo de entrada (original)
│ └── Extract_Prueba.py # Extracción de los datos desde el archivo
├── Load
│ ├── init.py
│ └── Load_Prueba.py # Carga de los datos
├── Transform
│ ├── init.py
│ └── Transform_Prueba.py # Limpieza de datos (relleno de valores nulos(con moda o mediana), eliminación de duplicados)
├── .gitignore
├── Main.py # Archivo principal que orquesta el proceso
├── README.md # Este archivo
└── requirements.txt # Dependencias del proyecto


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

## Instalación

1. **Clonar el repositorio**:

    ```bash
    git clone https://github.com/tu_usuario/proyecto-limpieza-datos.git
    cd proyecto-limpieza-datos
    ```

