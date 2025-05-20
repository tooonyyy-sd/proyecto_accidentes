import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



df1 = pd.read_excel('../data/processed/accidentes_victimas_comun_auton.xlsx')
df1.head()


## visualization of df2:
ruta = '../data/processed/victimas_segun_medio_trans.xlsx'
def cargar_victimas_segun_medio_trans(ruta):
    """
    Carga el archivo Excel de víctimas según medio de transporte con MultiIndex en columnas y la primera columna como índice.
    Asigna nombres a los niveles de índice y columnas.
    Devuelve el DataFrame resultante.
    """
    df2 = pd.read_excel(
        ruta,
        header=[0, 1],    # Dos primeras filas como MultiIndex en columnas
        index_col=0,      # Primera columna como índice
        engine='openpyxl'
    )
    df2.index.name = 'CLASES DE USUARIOS'
    df2.columns.names = ['Categoría', 'Métrica']
    return df2

# Ejemplo de uso:
ruta = '../data/processed/victimas_segun_medio_trans.xlsx'
df2 = cargar_victimas_segun_medio_trans(ruta)
df2.head()



## visualization of df3:
# 1) Ajusta esta ruta si tu WD es otra
ruta = '../data/processed/victimas_dias_mes.xlsx'

def cargar_victimas_dias_mes(ruta):
    """
    Carga el archivo Excel de víctimas por día del mes con MultiIndex en columnas y la primera columna como índice.
    Asigna nombres a los niveles de índice y columnas.
    Devuelve el DataFrame resultante.
    """
    df3 = pd.read_excel(
        ruta,
        header=[0, 1],      # Dos filas de encabezado para MultiIndex
        index_col=0,        # La primera columna será el índice (Día del mes)
        engine='openpyxl'
    )
    df3.index.name = 'Día del mes'
    df3.columns.names = ['Mes', 'Tipo']
    return df3

# Ejemplo de uso:
ruta = '../data/processed/victimas_dias_mes.xlsx'
df3 = cargar_victimas_dias_mes(ruta)
df3.head()

## visualization of df4:
def cargar_con_victimas_hora_inter(ruta):
    """
    Carga el archivo Excel de accidentes con víctimas por hora e intersección.
    Usa la segunda fila como cabecera y la primera columna como índice.
    Renombra el índice y las columnas para mayor claridad.
    Devuelve el DataFrame resultante.
    """
    df4 = pd.read_excel(
        ruta,
        header=1,      # la segunda fila contiene los nombres de las columnas
        index_col=0,   # la primera columna (“HORA”) como índice
        engine='openpyxl'
    )
    df4.index.name = 'HORA'
    df4.columns.name = None
    df4.columns = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo', 'TOTAL']
    return df4

# Ejemplo de uso:
ruta = '../data/processed/con_victimas_hora_inter.xlsx'
df4 = cargar_con_victimas_hora_inter(ruta)
df4.head()


## visualization of df5:
def cargar_infracciones_inter(ruta):
    """
    Carga el archivo Excel de infracciones en intersecciones.
    Usa la tercera fila como cabecera y la primera columna como índice.
    Renombra el índice y las columnas para mayor claridad.
    Devuelve el DataFrame resultante.
    """
    df5 = pd.read_excel(
        ruta,
        header=2,      # la tercera fila contiene los nombres de las columnas
        index_col=0,   # la primera columna (“TIPO DE INFRACCIÓN”) como índice
        engine='openpyxl'
    )
    df5.index.name = 'Tipo de infracción'
    df5.columns.name = 'Vehículo'
    return df5

# Ejemplo de uso:
ruta = '../data/processed/infracc_inter.xlsx'
df5 = cargar_infracciones_inter(ruta)
df5.head()
