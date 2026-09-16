# Análisis del desempeño de plantas de tratamiento

## AquaLimpia S. A.

**Proyecto de Ciencia de Datos**

---

## 1. Objetivo del análisis

Analizar el desempeño operacional y ambiental de las plantas de **AquaLimpia S. A.**, identificando variables relacionadas con la calidad del efluente tratado y el cumplimiento de la normativa ambiental.

---

## 2. Proceso de análisis

El análisis se desarrolló mediante un **flujo de trabajo reproducible utilizando Python**, organizado en las siguientes etapas:

1. Carga y revisión de los datos.
2. Limpieza y preparación.
3. Análisis exploratorio de las variables.
4. Aplicación de análisis estadístico mediante NumPy y SciPy.
5. Comparación del desempeño entre plantas.
6. Creación de gráficos y dashboard con **Plotly**.
7. Interpretación de los resultados.

---

## 3. Variables analizadas

Las principales variables consideradas en el análisis fueron:

* **Caudal de entrada:** volumen de agua residual recibido diariamente.
* **DBO de entrada:** carga orgánica presente antes del tratamiento.
* **DBO de salida:** carga orgánica presente después del tratamiento.
* **Energía de aireación:** energía utilizada durante el proceso de tratamiento.
* **Planta:** instalación donde se realizó el tratamiento.
* **Cumplimiento de norma:** indica si el efluente tratado cumple con los parámetros establecidos.

---

## 4. Análisis estadístico con NumPy y SciPy

Para complementar el análisis exploratorio se utilizaron **NumPy y SciPy** mediante scripts modulares, permitiendo separar las funciones estadísticas del notebook principal y facilitar la reutilización del código.

### Análisis con NumPy

Mediante **NumPy** se calcularon estadísticas descriptivas de la DBO de salida y la eficiencia de remoción de DBO.

Los principales resultados fueron:

* **DBO de salida promedio:** 36,18 mg/L.
* **DBO de salida mínima:** 10,20 mg/L.
* **DBO de salida máxima:** 79,00 mg/L.
* **Eficiencia promedio de remoción de DBO:** 87,09 %.

Estos resultados permiten conocer el comportamiento general de la DBO después del proceso de tratamiento y evaluar la reducción de la carga orgánica.

### Análisis con SciPy

Mediante **SciPy** se aplicó la correlación de Pearson para estudiar la relación entre las principales variables operacionales.

Se obtuvieron los siguientes resultados:

* **DBO de entrada vs. DBO de salida:** correlación fuerte y positiva (r = 0,759), estadísticamente significativa (p < 0,001).
* **Caudal de entrada vs. DBO de salida:** correlación débil y positiva (r = 0,104), no estadísticamente significativa (p = 0,144).

Los resultados indican que la DBO de entrada presenta una asociación lineal más clara con la DBO de salida, mientras que el caudal de entrada, considerado de forma individual, no muestra una relación lineal estadísticamente significativa con la DBO de salida.

---

## 5. Visualización de los datos

Se construyó un **dashboard exploratorio** para comparar el desempeño de las plantas y analizar las relaciones entre las principales variables operacionales y ambientales.

### El dashboard permite analizar:

* La relación entre **caudal de entrada y DBO de salida**.
* La relación entre **DBO de entrada y DBO de salida**.
* El consumo promedio de **energía de aireación por planta**.
* El nivel de **cumplimiento normativo** de las diferentes plantas.

---

## 6. Resultados

El análisis permitió identificar diferencias en el desempeño de las plantas y registros con niveles elevados de **DBO de salida**.

El análisis estadístico mostró una **eficiencia promedio de remoción de DBO de 87,09 %**. Además, se identificó una **correlación fuerte y positiva entre la DBO de entrada y la DBO de salida (r = 0,759)**, mientras que el caudal de entrada presentó una correlación débil con la DBO de salida (r = 0,104).

Las visualizaciones complementan estos resultados, facilitando la comparación del comportamiento de las plantas y la identificación de situaciones que podrían requerir una mayor revisión operacional.

---

## 7. Conclusión

La aplicación de **scripts modulares** permitió organizar el análisis de AquaLimpia S. A. de manera estructurada y reutilizable, separando las funciones estadísticas y de procesamiento del notebook principal.

Mediante **NumPy** se obtuvieron estadísticas descriptivas y una eficiencia promedio de remoción de DBO de **87,09 %**, mientras que **SciPy** permitió determinar que existe una correlación fuerte y positiva entre la DBO de entrada y la DBO de salida (**r = 0,759**). Por otra parte, la relación entre el caudal de entrada y la DBO de salida fue débil y no estadísticamente significativa.

La integración de estos análisis con las visualizaciones desarrolladas en **Plotly** permite comprender mejor el comportamiento de las plantas y disponer de información que puede apoyar la revisión de su desempeño operacional y ambiental.

---

## 8. Herramientas utilizadas

**Python | Pandas | NumPy | SciPy | Joblib | Plotly | Jupyter Notebook**

---

**Herramientas utilizadas:** Python | Pandas | Plotly | Numpy | SciPy | Jupyter Notebook
