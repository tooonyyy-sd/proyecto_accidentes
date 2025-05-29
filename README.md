# Proyecto I – EDA/ETL
## 📊 Preguntas de investigación

1. **Visión Global**  
   - ¿Cómo se distribuye el total de accidentes y víctimas según gravedad (fallecidos, heridos graves, heridos leves)?

2. **Análisis Geográfico**  
   - ¿Qué Comunidades Autónomas presentan las tasas más altas de accidentes con víctimas por 100 000 habitantes?

3. **Patrones Temporales**  
   - ¿Cuál es la evolución mensual de accidentes con víctimas a lo largo de 2023?

4. **Perfil de la Víctima**  
   - ¿Qué grupos de edad presentan mayor incidencia de accidentes con víctimas?

5. **Tipo de Accidente y Situación**  
   - ¿Qué tipos de siniestro (colisión frontal, salida de vía, atropello…) son más frecuentes?

6. **Factores Conexos y Correlaciones**  
   - ¿Existe relación entre el uso de cinturón/casco y la gravedad de las lesiones?

---

# 🚗 Proyecto: Análisis de Accidentes de Tráfico 2023

> **Descripción:**  
> Análisis exploratorio y visualización de datos de accidentes de tráfico en 2023, enfocado en:
>
> - **Accidentes con víctimas:** Totales y desglosados (mortales, heridos hospitalizados y no hospitalizados).
> - **Evolución mensual:** Víctimas por mes.
> - **Medio de transporte:** Porcentaje de implicados y víctimas (conductor, pasajero, peatón).
> - **Franja horaria:** Accidentes por hora e intersección.
> - **Infracciones:** Distribución por tipo de vehículo en intersecciones.

---

## 📁 Estructura del repositorio

```
proyecto_accidentes/
├── data/
│   ├── raw/                     # Datos originales
│   └── processed/               # Datos procesados
│       ├── accidentes_victimas_comun_auton.xlsx
│       ├── victimas_dias_mes.xlsx
│       ├── victimas_segun_medio_trans.xlsx
│       ├── con_victimas_hora_inter.xlsx
│       └── infracc_inter.xlsx
├── images/                      # Gráficos generados
│   ├── victimas_por_mes.png
│   └── vision_global_accidentes_heridos.png
├── notebooks/                   # Notebooks (EDA, informes)
│   └── EDA.ipynb
├── src/                         # Código fuente
│   ├── transformation.py
│   ├── exploration.py
│   └── visualization.py
├── README.md
└── requirements.txt
```

## ⚙️ Instalación rápida

```bash
git clone https://github.com/tooonyyy-sd/proyecto_accidentes.git
cd proyecto_accidentes

# Crear entorno virtual (elige uno)
python -m venv venv1
source venv1/Scripts/activate      # Windows Git Bash

# o con conda
conda create -n venv1 python=3.9    
conda activate venv1

# Instalar dependencias
pip install -r requirements.txt
```

---

## 🛠️ Uso

### 1. Transformación de datos

- **`agregar_total_victimas(df1)`**: Añade columna total_de_victimas.
- **`calcular_porcentajes_victimas(df2)`**: Porcentajes por medio de transporte.
- **`agrupar_por_franja_horaria(df4, franjas)`**: Resume accidentes por franjas horarias.
- **`agrupar_columnas_df5(df5)`**: Agrupa tipologías de vehículos.

```python
from src.transformation import *
import pandas as pd

df1 = pd.read_excel('data/processed/accidentes_victimas_comun_auton.xlsx')
df1 = agregar_total_victimas(df1)
print(df1.head())
```

### 2. Exploración de datos

- Funciones en `src/exploration.py` para cargar y visualizar muestras:
  - `cargar_victimas_segun_medio_trans(...)`
  - `cargar_victimas_dias_mes(...)`
  - ...

### 3. Visualización

- En `src/visualization.py`:
  - **`vision_global_accidentes_heridos(df1)`**: Totales y gráfico.
  - **`visualizar_victimas_por_mes(df3)`**: Gráfico mensual.

```bash
python src/visualization.py
```

---
## 📈 Resultados destacados

- **Visión global:**  
  - 473 286 accidentes con víctimas  
    - Media mensual: 10 663 (σ ≈ 22 849)  
  - 3 360 accidentes mortales  
    - Media mensual: 176 (σ ≈ 372)  
  - 18 530 heridos hospitalizados  
    - Media mensual: 975 (σ ≈ 2 059)  
  - 248 532 heridos no hospitalizados  
    - Media mensual: 13 081 (σ ≈ 28 051)

- **Correlaciones:**  
  Todas las variables clave (accidentes con víctimas, mortales, fallecidos, heridos hospitalizados y no hospitalizados) muestran coeficientes de Pearson > 0,99, indicando una fuerte multicolinealidad.

- **Distribución de Accidentes mortales y Fallecidos:**  
  Los boxplots revelan varios outliers altos en algunas Comunidades Autónomas, con valores máximos que superan ampliamente la mediana.


Revisar la carpeta `images` para las imagenes qeu muestran estos resultados```
