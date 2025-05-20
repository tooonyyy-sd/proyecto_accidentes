import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


## Visualization of df1:
def vision_global_accidentes_heridos(df1):
    """
    Muestra por pantalla el total de:
      - Accidentes con víctimas
      - Accidentes mortales
      - Heridos hospitalizados
      - Heridos no hospitalizados
    y dibuja un gráfico de barras con la misma distribución.
    """
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
    plt.show()

vision_global_accidentes_heridos(df1)








## Gráfico de los totales mensuales de víctimas por día del mes
plt.figure(figsize=(14,6))
victimas_mensual['Total víctimas día'].plot(kind='bar', color='skyblue')
plt.title('Víctimas por día del mes (Total mensual)')
plt.xlabel('Día del mes')
plt.ylabel('Número de víctimas')
plt.tight_layout()
plt.show()

# El gráfico muestra la suma total de víctimas por cada día del mes, considerando todos los meses juntos.
# No corresponde a un mes concreto, sino al total agregado de todos los meses disponibles en el DataFrame.





## Gráfico de la evolución mensual de víctimas a lo largo de 2023
# Usamos la serie 'victimas_por_mes' y las etiquetas de los meses

plt.figure(figsize=(12,6))
# Asegúrate de que x e y tengan la misma longitud (12)
sns.lineplot(x=meses_nombres, y=victimas_por_mes.values[:12], marker='o')
plt.title('Evolución mensual de víctimas a lo largo de 2023')
plt.xlabel('Mes')
plt.ylabel('Número de víctimas')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()