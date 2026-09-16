from scipy import stats


def correlacion_pearson(df, variable_x, variable_y):
    """
    Calcula la correlación de Pearson entre
    dos variables del DataFrame.
    """

    datos = df[
        [variable_x, variable_y]
    ].dropna()

    r, p = stats.pearsonr(
        datos[variable_x],
        datos[variable_y]
    )

    return r, p


def interpretar_correlacion(r):
    """
    Interpreta la intensidad y dirección
    de una correlación.
    """

    valor = abs(r)

    if valor < 0.30:
        intensidad = "débil"
    elif valor < 0.70:
        intensidad = "moderada"
    else:
        intensidad = "fuerte"

    if r > 0:
        direccion = "positiva"
    elif r < 0:
        direccion = "negativa"
    else:
        direccion = "sin relación lineal"

    return intensidad, direccion


def interpretar_significancia(p):
    """
    Interpreta el p-valor utilizando
    un nivel de significancia de 0.05.
    """

    if p < 0.05:
        return "La relación es estadísticamente significativa."
    else:
        return "La relación no es estadísticamente significativa."