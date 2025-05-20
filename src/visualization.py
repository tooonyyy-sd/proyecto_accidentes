import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


##RESPONDER A LA VISION GLOBAL
#Objetivo: ¿Cómo se distribuyen los accidentes (entre "accidentes con víctimas" y "accidentes mortales") y los heridos (segun "heridos hospitalizados" y "heridos no hospitalizados")?
# Seleccionamos las columnas relevantes del total mensual (fila 'Total')
cols_accidentes = [col for col in df3.columns if "TOTAL" in col]
cols_mortales = [col for col in df3.columns if "MORTALES A 30 DÍAS" in col]
cols_heridos_hosp = [col for col in df3.columns if "HERIDOS HOSPITALIZADOS" in col]
cols_heridos_nohosp = [col for col in df3.columns if "HERIDOS NO HOSPITALIZADOS" in col]

# Extraemos los totales de la fila 'Total'
totales = df3.loc["Total"]

# Sumamos los valores de cada grupo
accidentes_victimas = totales[cols_accidentes].sum()
accidentes_mortales = totales[cols_mortales].sum()
heridos_hospitalizados = totales[cols_heridos_hosp].sum()
heridos_no_hospitalizados = totales[cols_heridos_nohosp].sum()

# Mostramos la distribución
print("Accidentes con víctimas:", accidentes_victimas)
print("Accidentes mortales:", accidentes_mortales)
print("Heridos hospitalizados:", heridos_hospitalizados)
print("Heridos no hospitalizados:", heridos_no_hospitalizados)

# Visualización
labels = ['Accidentes con víctimas', 'Accidentes mortales', 'Heridos hospitalizados', 'Heridos no hospitalizados']
values = [accidentes_victimas, accidentes_mortales, heridos_hospitalizados, heridos_no_hospitalizados]

plt.figure(figsize=(8,5))
sns.barplot(x=labels, y=values)
plt.title("Distribución de accidentes y heridos")
plt.ylabel("Cantidad")
plt.xticks(rotation=20)
plt.show()







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