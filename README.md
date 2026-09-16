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
4. Comparación del desempeño entre plantas.
5. Creación de gráficos y dashboard con **Plotly**.
6. Interpretación de los resultados.

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

## 4. Visualización de los datos

Se construyó un **dashboard exploratorio** para comparar el desempeño de las plantas y analizar las relaciones entre las principales variables operacionales y ambientales.

### El dashboard permite analizar:

* La relación entre **caudal de entrada y DBO de salida**.
* La relación entre **DBO de entrada y DBO de salida**.
* El consumo promedio de **energía de aireación por planta**.
* El nivel de **cumplimiento normativo** de las diferentes plantas.

---

## 5. Resultados

El análisis permite identificar diferencias en el desempeño de las plantas, detectar registros con niveles elevados de **DBO de salida** y observar posibles relaciones entre las variables operacionales y los incumplimientos de la normativa.

Las visualizaciones facilitan la comparación de los resultados y permiten reconocer situaciones que podrían requerir una mayor revisión operacional.

---

## 6. Conclusión

El uso de **Python y Plotly** permite analizar y visualizar los datos de AquaLimpia S. A. de forma reproducible, facilitando la identificación de patrones y apoyando la toma de decisiones.

El análisis de variables como el **caudal de entrada, DBO de entrada y salida, energía de aireación y cumplimiento normativo** permite comparar el desempeño de las distintas plantas e identificar posibles relaciones entre las condiciones operacionales y la calidad del efluente tratado.

De esta manera, los resultados obtenidos pueden contribuir a detectar situaciones de incumplimiento y orientar mejoras en la operación de las plantas.

---

**Herramientas utilizadas:** Python | Pandas | Plotly | Numpy | SciPy | Jupyter Notebook
