import numpy as np


def estadisticas_variable(datos):
    """
    Calcula estadísticas descriptivas básicas
    de una variable numérica utilizando NumPy.
    """

    datos = np.asarray(datos.dropna(), dtype=float)

    resultados = {
        "cantidad": len(datos),
        "promedio": np.mean(datos),
        "mediana": np.median(datos),
        "desviacion_estandar": np.std(datos),
        "minimo": np.min(datos),
        "maximo": np.max(datos)
    }

    return resultados


def eficiencia_remocion(dbo_entrada, dbo_salida):
    """
    Calcula el porcentaje promedio de remoción de DBO.
    """

    entrada = np.asarray(dbo_entrada, dtype=float)
    salida = np.asarray(dbo_salida, dtype=float)

    # Evitar divisiones por cero
    mascara = entrada != 0

    eficiencia = (
        (entrada[mascara] - salida[mascara])
        / entrada[mascara]
    ) * 100

    return np.mean(eficiencia)