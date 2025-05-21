import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import src.exploration as exp
import src.visualization as vis
import src.transformation as ts



## DEFINCIÓN DE RUTAS Y VARIABLES
ruta2 = '../data/processed/victimas_segun_medio_trans.xlsx'
ruta3 = '../data/processed/victimas_dias_mes.xlsx'
ruta4 = '../data/processed/con_victimas_hora_inter.xlsx'
ruta5 = '../data/processed/infracc_inter.xlsx'

df1 = pd.read_excel('../data/processed/accidentes_victimas_comun_auton.xlsx')
df2 = pd.read_excel(
    ruta2,
    header=[0, 1],  
    index_col=0,   
    engine='openpyxl'
)

df2.index.name = 'CLASES DE USUARIOS'
df2.columns.names = ['Categoría', 'Métrica']
df3 = pd.read_excel(
    ruta3,
    header=[0, 1],      # Dos filas de encabezado para MultiIndex
    index_col=0,        # La primera columna será el índice (Día del mes)
    engine='openpyxl'
)

# 3) Pon nombre claro al índice y a los niveles de columnas
df3.index.name = 'Día del mes'
df3.columns.names = ['Mes', 'Tipo']
df4 = pd.read_excel(
    ruta4,
    header=1,      
    index_col=0,   
    engine='openpyxl'
)
df4.index.name = 'HORA'
df4.columns.name = None
df4.columns = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo', 'TOTAL']
franjas = {
    '00:00-05:59': ['00:00-00:59', '01:00-01:59', '02:00-02:59', '03:00-03:59', '04:00-04:59', '05:00-05:59'],
    '06:00-11:59': ['06:00-06:59', '07:00-07:59', '08:00-08:59', '09:00-09:59', '10:00-10:59', '11:00-11:59'],
    '12:00-17:59': ['12:00-12:59', '13:00-13:59', '14:00-14:59', '15:00-15:59', '16:00-16:59', '17:00-17:59'],
    '18:00-23:59': ['18:00-18:59', '19:00-19:59', '20:00-20:59', '21:00-21:59', '22:00-22:59', '23:00-23:59']
}
df5 = pd.read_excel(
        ruta5,
        header=2,      
        index_col=0,   
        engine='openpyxl'
    )
df5.index.name = 'Tipo de infracción'
df5.columns.name = 'Vehículo'
ruta5 = '../data/processed/infracc_inter.xlsx'



## TRANSFORMACIONES, EXPLORACIÓN Y VISUALIZACIÓN
if __name__ == "__main__":
    exp.cargar_victimas_segun_medio_trans(ruta2) 
    exp.cargar_victimas_dias_mes(ruta3)
    exp.cargar_con_victimas_hora_inter(ruta4)
    exp.cargar_infracciones_inter(ruta5)

    ts.agregar_total_victimas(df1)
    ts.calcular_porcentajes_victimas(df2)
    ts.agrupar_por_franja_horaria(df4, franjas)
    ts.agrupar_columnas_df5(df5)

    vis.vision_global_accidentes_heridos(df1)
    vis.visualizar_victimas_por_mes(df3)
