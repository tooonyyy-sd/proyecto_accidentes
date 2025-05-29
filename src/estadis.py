import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys, os
from scipy import stats

df1 = pd.read_excel('../data/processed/accidentes_victimas_comun_auton.xlsx')

# 1. Estadística descriptiva para df1
def descriptive_stats_df1(df1):
    cols = [
        'ACCIDENTES CON\nVÍCTIMAS',
        'ACCIDENTES\nMORTALES',
        'FALLECIDOS',
        'HERIDOS\nHOSPITALIZADOS',
        'HERIDOS NO\nHOSPITALIZADOS'
    ]
    # Describe centralidad y dispersión
    descr = df1[cols].describe().T
    # Matriz de correlaciones de Pearson
    corr = df1[cols].corr()
    return descr, corr
descriptive_stats_df1(df1)





def graficos_descriptivos_df1(df1):
    cols = [
        'ACCIDENTES CON\nVÍCTIMAS',
        'ACCIDENTES\nMORTALES',
        'FALLECIDOS',
        'HERIDOS\nHOSPITALIZADOS',
        'HERIDOS NO\nHOSPITALIZADOS'
    ]
    descr = df1[cols].describe().T
    corr = df1[cols].corr()

    # Gráfico de medias y desviaciones estándar
    plt.figure(figsize=(10, 5))
    plt.bar(descr.index, descr['mean'], yerr=descr['std'], capsize=5, color='skyblue')
    plt.ylabel('Media (con desviación estándar)')
    plt.title('Media y desviación estándar de variables principales')
    plt.xticks(rotation=20, ha='right')
    plt.tight_layout()
    plt.savefig('../images/medias_desviaciones.png')
    plt.show()

    # Boxplot para Accidentes mortales y Fallecidos
    plt.figure(figsize=(6, 5))
    sns.boxplot(data=df1[['ACCIDENTES\nMORTALES', 'FALLECIDOS']], showmeans=True)
    plt.title('Distribución de Accidentes mortales y Fallecidos')
    plt.ylabel('Cantidad')
    plt.tight_layout()
    plt.savefig('../images/boxplot_mortales_fallecidos.png')
    plt.show()

    # Heatmap de correlaciones
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Matriz de correlaciones (Pearson)')
    plt.tight_layout()
    plt.savefig('../images/heatmap.png')
    plt.show()

# Ejemplo de uso:
graficos_descriptivos_df1(df1)