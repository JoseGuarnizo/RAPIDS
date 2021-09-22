# Implementación de un Ambiente de Ciencia de Datos a través de la librería RAPIDS

![Logo principal de la librería](https://github.com/JoseGuarnizo/RAPIDS/blob/master/imagenes/rapids.PNG)

### Tabla de Contenidos

- Introducción
- Exploración del Repositorio
- Puebas y Resultados con RAPIDS


### Introducción
Se da realce a principales funcionalidades, características y todo su conjunto de bibliotecas que tiene la librería RAPIDS, se utilizó la Plataforma Cloud BlazingSQL para la implementación, donde resalta el proceso de construcción de un Ambiente de Ciencia de Datos utilizando RAPIDS para los procesos de ETL, Machine Learning y Visualización, se implementó una contraparte utilizando librerías que aún no tiene soporte para GPU como Pandas para el proceso de ETL, para el proceso de Machine Learning con Scikit-learn y para la visualización con Matplotlib, la comparación con las librerías tradicionales permite resaltar la aceleración o rapidez que tiene RAPIDS cuando trabaja con grandes volúmenes de información.

### Exploración del Repositorio

- `Documento_General_Trabajo` - "Documentación de como instalar y utilizar toda la librería RAPIDS cojuntamente con un Artículos Científicos"
- `datasets` - "Resultados de datasets que se utilizaron en el proceso de ETL, ML y Visualización"
- `ejemplos_datascience_Rapids` - "Algunos ejemplos adicionales utilizando algunas caraterísticas de la librería RAPIDS con sus bibliotecas"
- `imagenes` - "Captura de imagenes de instalación de la librería RAPIDS localmente y plataformas cloud"
- `implementación_RAPIDS` - "Toda la construcción e implementación de RAPIDS utilizando las bibliotecas para todo el proceso de Ciencia de Datos y también implementación con librerías tradicionales"

### Pruebas y Resultados con RAPIDS

En base a los escenarios propuestos comparando los tiempos de aceleración de RAPIDS juntamente con las librerías tradicionales para ciencia de datos tanto en los procesos ETL, machine learning y visualización (representación de los datos en forma gráfica) destaca RAPIDS, acelera el flujo de extremo a extremo y cumple su principal objetivo de trabajar de forma acelerada utilizando las características de las GPUs de NVIDIA (GPU Tesla T4), esto da un realce significativo para utilizar la librería RAPIDS cuando se va a trabajar con grandes volúmenes de información.

#### Proceso de Extracción, Transformación y Carga (ETL)

| Librería | Fase | Tiempo Aceleración (segundos) | Número de Datos | Tamaño Archivo |
| --- | --- | :---: | :---: | :---: |
| Rapids (cudf) | Extracción | 0.70 s | 200.000 | 252 MB |
| Rapids (cudf) | Transformación | 7.24 s | 200.000 | 252 MB |
| Rapids (cudf) | Carga | 0.51 s | 200.000 | 252 MB |
| Pandas | Extracción | 3.17 s | 200.000 | 252 MB |
| Pandas | Transformación | 8.14 s | 200.000 | 252 MB |
| Pandas | Carga | 2.10 s | 200.000 | 252 MB |

#### Proceso de Machine Learning (ML)

| Librería | Fase | Tiempo Aceleración (segundos) | Número de Datos | Tamaño Archivo |
| --- | --- | :---: | :---: | :---: |
| Rapids (cuml) | Preprocesamiento | 0.13 s | 196.867 | 41.6 MB |
| Scikit-learn | Preprocesamiento | 0.14 s | 196.867 | 41.6 MB |

| Librería | Algoritmo ML | Tiempo Aceleración (segundos) | Número de Datos | Tamaño Archivo |
| --- | --- | :---: | :---: | :---: |
| Rapids (cuml) | Regresión Lineal | 0.009 s  | 196.867 | 41.6 MB |
| Rapids (cuml) | Regresión Logística | 16.42 s | 196.867 | 41.6 MB |
| Scikit-learn | Regresión Lineal | 0.01 s | 196.867 | 41.6 MB |
| Scikit-learn | Regresión Logística | 484.30 s | 196.867 | 41.6 MB |

#### Proceso de Visualización

| Librería | Tipo Gráfico Estadístico | Tiempo Aceleración (segundos) | Número de Datos | Tamaño Archivo |
| --- | --- | :---: | :---: | :---: |
| Rapids (cuxfilter) | Barras | 4.25 s  | 196.867 | 41.6 MB |
| Rapids (cuxfilter) | Líneas | 0.38 s  | 196.867 | 41.6 MB |
| Matplotlib | Barras | 191.22 s  | 196.867 | 41.6 MB |
| Matplotlib | Líneas | 3.38 s  | 196.867 | 41.6 MB |


### Información Adicional

- La librería Rapids la puedes encontrar aquí [Rapids](https://rapids.ai/)
- La plataforma BlanzingSQL la puedes encontrar aquí [BlazingSQL](https://blazingsql.com/)


