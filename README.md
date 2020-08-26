# Implementación de un Ambiente de Ciencia de Datos a través de la librería RAPIDS

### Tabla de Contenidos

Introducción
Exploración del Repositorio
Puebas y Resultados con Rapids


### Introducción
Se da realce a principales funcionalidades, características y todo su conjunto de bibliotecas que tiene la librería Rapids, además, se utilizó la Plataforma Cloud BlazingSQL para la implementación, donde resalta el proceso de construcción de un Ambiente de Ciencia de Datos utilizando Rapids para los procesos de ETL, Machine Learning y Visualización, se implemento una contraparte utilizando librerías que aún no tiene soporte para GPU como Pandas para el proceso de ETL, para el proceso de Machine Learning con Scikit-learn y para la visualización con Matplotlib, la comparación con las librerías tradicionales permite resaltar la aceleración o rapidez que tiene Rapids cuando trabaja con grandes volúmenes de información.

### Exploración Rep



### Pruebas y Resultados con Rapids

| Librería | Algoritmo ML | Tiempo Aceleración (segundos) | Número de Datos |
| --- | --- | --- | --- |
| Rapids (cuml) | Regresión Lineal | 0.009 s  | 157.493 |
| Rapids (cuml) | Regresión Logística | 16.42 s | 157.493  |
| Scikit-learn | Regresión Lineal | 0.018 s | 157.493 |
| Scikit-learn | Regresión Logística | 484.30 s | 157.493 |
