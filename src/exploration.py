import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


## visualizar df1:
df1 = pd.read_excel('../data/processed/accidentes_victimas_comun_auton.xlsx')
df1.head()


## visualizar df2:
ruta2 = '../data/processed/victimas_segun_medio_trans.xlsx'
def cargar_victimas_segun_medio_trans(ruta2):
   
    df2 = pd.read_excel(
        ruta2,
        header=[0, 1],    
        index_col=0,      
        engine='openpyxl'
    )
    df2.index.name = 'CLASES DE USUARIOS'
    df2.columns.names = ['Categoría', 'Métrica']
    return df2


ruta2 = '../data/processed/victimas_segun_medio_trans.xlsx'
df2 = cargar_victimas_segun_medio_trans(ruta2)
df2.head()



## visualizar df3:
ruta3 = '../data/processed/victimas_dias_mes.xlsx'

def cargar_victimas_dias_mes(ruta3):
    
    df3 = pd.read_excel(
        ruta3,
        header=[0, 1],      
        index_col=0,        
        engine='openpyxl'
    )
    df3.index.name = 'Día del mes'
    df3.columns.names = ['Mes', 'Tipo']
    return df3


ruta3 = '../data/processed/victimas_dias_mes.xlsx'
df3 = cargar_victimas_dias_mes(ruta3)
df3.head()

## visualizar df4:
def cargar_con_victimas_hora_inter(ruta4):

    df4 = pd.read_excel(
        ruta4,
        header=1,      
        index_col=0,   
        engine='openpyxl'
    )
    df4.index.name = 'HORA'
    df4.columns.name = None
    df4.columns = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo', 'TOTAL']
    return df4


ruta4 = '../data/processed/con_victimas_hora_inter.xlsx'
df4 = cargar_con_victimas_hora_inter(ruta4)
df4.head()


## visualizar df5:
def cargar_infracciones_inter(ruta5):
    """
    Carga el archivo Excel de infracciones en intersecciones.
    Usa la tercera fila como cabecera y la primera columna como índice.
    Renombra el índice y las columnas para mayor claridad.
    Devuelve el DataFrame resultante.
    """
    df5 = pd.read_excel(
        ruta5,
        header=2,     
        index_col=0,   
        engine='openpyxl'
    )
    df5.index.name = 'Tipo de infracción'
    df5.columns.name = 'Vehículo'
    return df5


ruta5 = '../data/processed/infracc_inter.xlsx'
df5 = cargar_infracciones_inter(ruta5)
df5.head()
