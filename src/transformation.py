import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

## Transformation in df1:
def agregar_total_victimas(df1):
    """
    Agrega una columna 'total_de_victimas' al DataFrame sumando solo las columnas relevantes de víctimas.
    """
    columnas_sumar = [
        'ACCIDENTES CON\nVÍCTIMAS',
        'ACCIDENTES\nMORTALES',
        'FALLECIDOS',
        'HERIDOS\nHOSPITALIZADOS',
        'HERIDOS NO\nHOSPITALIZADOS'
    ]
    # Solo suma las columnas que existen en el DataFrame
    columnas_existentes = [col for col in columnas_sumar if col in df1.columns]
    df1['total_de_victimas'] = df1[columnas_existentes].sum(axis=1)
    return df1

## Transformation in df2:
# Definicion df2

ruta2 = '../data/processed/victimas_segun_medio_trans.xlsx'
df2 = pd.read_excel(
    ruta2,
    header=[0, 1],  
    index_col=0,   
    engine='openpyxl'
)

df2.index.name = 'CLASES DE USUARIOS'
df2.columns.names = ['Categoría', 'Métrica']

#Funcion df2
def calcular_porcentajes_victimas(df2):
    """
    Calcula el porcentaje de cada subcolumna de Conductor, Pasajero y Peatón respecto a Total,
    para las subcolumnas especificadas. Devuelve un DataFrame con los porcentajes redondeados a 2 decimales.
    """
    columnas = ['Total', 'Conductor', 'Pasajero', 'Peatón']
    subcolumnas = ['Nº implicados', 'VÍCTIMAS', 'FALLECIDOS', 'HOSPITALIZADOS', 'NO\nHOSPITALIZADOS']

    porcentajes = {}
    for col in columnas:
        for subcol in subcolumnas:
            key = (col, subcol)
            if col == 'Total':
                porcentajes[key] = df2[(col, subcol)]
            else:
                porcentajes[key] = df2[(col, subcol)] / df2[('Total', subcol)] * 100

    df_porcentajes = pd.concat(porcentajes, axis=1)
    df2_porcentajes = df_porcentajes.round(2)
    return df2_porcentajes

# Ejemplo de uso:
df2_porcentajes = calcular_porcentajes_victimas(df2)
df2_porcentajes.head()

## Transformation of df4:
#Definicion df4

ruta4 = '../data/processed/con_victimas_hora_inter.xlsx'
df4 = pd.read_excel(
    ruta4,
    header=1,      
    index_col=0,   
    engine='openpyxl'
)
df4.index.name = 'HORA'
df4.columns.name = None
df4.columns = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo', 'TOTAL']

#Funcion df4
def agrupar_por_franja_horaria(df4, franjas):
    """
    Agrupa y suma los valores de un DataFrame por las franjas horarias definidas en el diccionario 'franjas'.
    Devuelve un nuevo DataFrame con las franjas como índice.
    """
    df_franjas = pd.DataFrame([
        df4.loc[horas].sum() for horas in franjas.values()
    ], index=franjas.keys())
    return df_franjas

# Ejemplo de uso:
franjas = {
    '00:00-05:59': ['00:00-00:59', '01:00-01:59', '02:00-02:59', '03:00-03:59', '04:00-04:59', '05:00-05:59'],
    '06:00-11:59': ['06:00-06:59', '07:00-07:59', '08:00-08:59', '09:00-09:59', '10:00-10:59', '11:00-11:59'],
    '12:00-17:59': ['12:00-12:59', '13:00-13:59', '14:00-14:59', '15:00-15:59', '16:00-16:59', '17:00-17:59'],
    '18:00-23:59': ['18:00-18:59', '19:00-19:59', '20:00-20:59', '21:00-21:59', '22:00-22:59', '23:00-23:59']
}

df4_franjas = agrupar_por_franja_horaria(df4, franjas)
df4_franjas

## Transformation of df5:
#Definicion df5
ruta5 = '../data/processed/infracc_inter.xlsx'
df5 = pd.read_excel(
        ruta5,
        header=2,      
        index_col=0,   
        engine='openpyxl'
    )
df5.index.name = 'Tipo de infracción'
df5.columns.name = 'Vehículo'


#Funcion df5
def agrupar_columnas_df5(df5):
    """
    Agrupa las columnas de df5 según las categorías solicitadas y devuelve un nuevo DataFrame con las columnas agrupadas.
    """
    df5_agrupado = pd.DataFrame({
        'Total': df5['Total'],
        'Sin motor': df5['Bicicleta'] + df5['VMP'],
        'a motor': df5['Ciclomotor'] + df5['Motocicleta'] + df5['Turismo'] + df5['Furgoneta'],
        'a motor grande': df5['Camión =< 3.500 kg'] + df5['Camión > 3.500 kg'] + df5['Autobús'],
        'otro vehiculo': df5['Otro vehículo'],
        'se desconoce': df5['Se desconoce']
    })
    return df5_agrupado

# Ejemplo de uso:
df5_agrupado_columnas = agrupar_columnas_df5(df5)
df5_agrupado_columnas.head()



