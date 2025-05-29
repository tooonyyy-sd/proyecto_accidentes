import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


## Visualizacion df1:
df1 = pd.read_excel('../data/processed/accidentes_victimas_comun_auton.xlsx')
def vision_global_accidentes_heridos(df1):
    

    # Cálculo de totales
    totales = {
        'Accidentes con víctimas': df1['ACCIDENTES CON\nVÍCTIMAS'].sum(),
        'Accidentes mortales': df1['ACCIDENTES\nMORTALES'].sum(),
        'Heridos hospitalizados': df1['HERIDOS\nHOSPITALIZADOS'].sum(),
        'Heridos no hospitalizados': df1['HERIDOS NO\nHOSPITALIZADOS'].sum()
    }
    # Imprimir totales
    for nombre, valor in totales.items():
        print(f"{nombre}: {valor}")
    # Gráfico
    sns.set_style('darkgrid')
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(totales.keys()), y=list(totales.values()))
    plt.title("Distribución de accidentes y heridos")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=20, ha='right')
    plt.tight_layout()
    plt.savefig('../images/vision_global_accidentes_heridos.png')
    plt.show()



vision_global_accidentes_heridos(df1)



## Visualizacion df3:
# Definir df3:
ruta3 = '../data/processed/victimas_dias_mes.xlsx'

df3 = pd.read_excel(
    ruta3,
    header=[0, 1],      
    index_col=0,    
    engine='openpyxl'
)
df3.index.name = 'Día del mes'
df3.columns.names = ['Mes', 'Tipo']

# Funcion 
def visualizar_victimas_por_mes(df3):
    
    # Encuentra todas las columnas cuyo segundo nivel contenga 'total'
    total_cols = [col for col in df3.columns if 'total' in str(col[1]).lower()]
    # Diccionario para almacenar el total de cada mes
    victimas_por_mes = {}
    for mes, tipo in total_cols:
        # Toma el valor de la última fila (total del mes)
        total_mes = df3[(mes, tipo)].iloc[-1]
        victimas_por_mes[mes.lower()] = total_mes

    # Ordena los meses
    meses_orden = [
        'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
        'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
    ]
    victimas_por_mes = {mes: victimas_por_mes[mes] for mes in meses_orden if mes in victimas_por_mes}

    # Gráfico
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=list(victimas_por_mes.keys()), y=list(victimas_por_mes.values()), marker='o')
    plt.title('Víctimas totales por mes en 2023 (valor de la última fila)')
    plt.xlabel('Mes')
    plt.ylabel('Número de víctimas')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('../images/victimas_por_mes.png')
    plt.show()

    return victimas_por_mes


visualizar_victimas_por_mes(df3)