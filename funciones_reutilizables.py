import pandas as pd
import numpy as np


def cargar_datos(ruta):
    """
    Carga el dataset de AquaLimpia y convierte la fecha
    al formato correspondiente.
    """
    df = pd.read_csv(
        ruta,
        sep=";",
        decimal=","
    )

    df["fecha_registro"] = pd.to_datetime(
        df["fecha_registro"]
    )

    return df


def seleccionar_variables(df):
    """
    Selecciona las variables utilizadas en el análisis.
    """
    variables = [
        "fecha_registro",
        "planta",
        "caudal_entrada_m3_d",
        "DBO_entrada_mg_L",
        "DBO_salida_mg_L",
        "energia_aeracion_kWh",
        "lodos_generados_kg_d",
        "cumplimiento_norma"
    ]

    return df[variables].copy()


def revisar_calidad(datos):
    """
    Revisa dimensiones, valores nulos y registros duplicados.
    """
    print("Cantidad de registros:", datos.shape[0])
    print("Cantidad de variables:", datos.shape[1])

    print("\nValores nulos:")
    print(datos.isnull().sum())

    print("\nRegistros duplicados:")
    print(datos.duplicated().sum())


def generar_resumen_planta(datos):
    """
    Calcula indicadores promedio para cada planta.
    """
    resumen = (
        datos.groupby("planta")
        .agg(
            caudal_promedio=("caudal_entrada_m3_d", "mean"),
            DBO_entrada_promedio=("DBO_entrada_mg_L", "mean"),
            DBO_salida_promedio=("DBO_salida_mg_L", "mean"),
            energia_promedio=("energia_aeracion_kWh", "mean"),
            lodos_promedio=("lodos_generados_kg_d", "mean"),
            cumplimiento=("cumplimiento_norma", "mean")
        )
        .reset_index()
    )

    resumen["cumplimiento_porcentaje"] = (
        resumen["cumplimiento"] * 100
    )

    return resumen.round(2)
    