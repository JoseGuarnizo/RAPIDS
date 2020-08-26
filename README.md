# Implementación de un Ambiente de Ciencia de Datos a través de la librería RAPIDS

### Tabla de Contenidos

- Introducción
- Exploración del Repositorio
- Puebas y Resultados con Rapids


### Introducción
Se da realce a principales funcionalidades, características y todo su conjunto de bibliotecas que tiene la librería Rapids, además, se utilizó la Plataforma Cloud BlazingSQL para la implementación, donde resalta el proceso de construcción de un Ambiente de Ciencia de Datos utilizando Rapids para los procesos de ETL, Machine Learning y Visualización, se implemento una contraparte utilizando librerías que aún no tiene soporte para GPU como Pandas para el proceso de ETL, para el proceso de Machine Learning con Scikit-learn y para la visualización con Matplotlib, la comparación con las librerías tradicionales permite resaltar la aceleración o rapidez que tiene Rapids cuando trabaja con grandes volúmenes de información.

### Exploración del Repositorio

- `Documento_General_Trabajo` - "Dcoumentación de como instalar y utilizar toda la librerpia Rapids cojuntamento con un Artículo Científico"
- `Reportes` - "Presentaciones de Rapids, enfocando los puntos pirncipales de la librería"
- `datasets` - "Resultados de datasets que se utilizaron en el proceso de ETL, ML y Visualización"
- `ejemplos_datascience_Rapids` - "Algunos ejemplos adicionales utilizando algunas caraterísticas de la librería Rapids con sus bibliotecas"
- `implmentación_Rapids` - "Toda la construcción e implementación de Rapids utilizando las bibliotecas para todo el proceso de Ciencia de Datos y también implementación con librerías tradicionales"

### Pruebas y Resultados con Rapids

#### Proceso de Extracción, Transformación y Carga (ETL)

| Librería | Fase | Tiempo Aceleración (segundos) | Número de Datos | Tamaño Archivo |
| --- | --- | :---: | :---: | :---: |
| Rapids (cudf) | Extracción | 0.70 s | 200.000 | 252 MB |
| Rapids (cudf) | Transformación | 7.24 s | 200.000 | 252 MB |
| Rapids (cudf) | Carga | 0.51 s | 200.000 | 252 MB |
| Pandas | Extracción | 3.17 s | 200.000 | 252 MB |
| Pandas | Transformación | 8.14 s | 200.000 | 252 MB |
| Pandas | Carga | 2.10 s | 200.000 | 252 MB |

#### Proceso de Machine Learning

| Librería | Fase | Tiempo Aceleración (segundos) | Número de Datos | Tamaño Archivo |
| --- | --- | :---: | :---: | :---: |
| Rapids (cuml) | Preprocesamiento | 0.13 s | 157.493 | 41.6 MB |
| Scikit-learn | Preprocesamiento | 0.14 s | 157.493 | 41.6 MB |

| Librería | Algoritmo ML | Tiempo Aceleración (segundos) | Número de Datos | Tamaño Archivo |
| --- | --- | :---: | :---: | :---: |
| Rapids (cuml) | Regresión Lineal | 0.009 s  | 157.493 | 41.6 MB |
| Rapids (cuml) | Regresión Logística | 16.42 s | 157.493  | 41.6 MB |
| Scikit-learn | Regresión Lineal | 0.018 s | 157.493 | 41.6 MB |
| Scikit-learn | Regresión Logística | 484.30 s | 157.493 | 41.6 MB |

#### Proceso de Visualización

| Librería | Tipo Gráfico Estadístico | Tiempo Aceleración (segundos) | Número de Datos | Tamaño Archivo |
| --- | --- | :---: | :---: | :---: |
| Rapids (cuxfilter) | Barras | 4.25 s  | 157.493 | 41.6 MB |
| Rapids (cuxfilter) | Líneas | 0.38 s  | 157.493 | 41.6 MB |
| Matplotlib | Barras | 191.22 s  | 157.493 | 41.6 MB |
| Matplotlib | Líneas | 3.38 s  | 157.493 | 41.6 MB |



