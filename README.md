# Proyecto de Grado: Análisis de la Encuesta Nacional de Consumo de Sustancias Psicoactivas (ENCSPA) 2019

## Descripción del Proyecto

Este proyecto constituye el trabajo de grado para la carrera de Ciencia de Datos. Utiliza los datos de la **Encuesta Nacional de Consumo de Sustancias Psicoactivas en Población General (ENCSPA) 2019**, realizada por el Departamento Administrativo Nacional de Estadística (DANE) de Colombia en colaboración con el Ministerio de Justicia y del Derecho.

El objetivo principal es realizar un análisis exploratorio de datos (EDA) completo y profundo que permita caracterizar el consumo de sustancias psicoactivas en la población colombiana de 12 a 65 años, identificar patrones de consumo, perfiles sociodemográficos y dinámicas del mercado ilegal.

## Estructura del Proyecto

```
Proyecto_Grado_ENCSPA/
│
├── data/
│   ├── raw/                    # Archivos CSV originales descargados del DANE
│   ├── interim/                # Archivos intermedios (limpieza inicial en Parquet)
│   └── processed/              # DataFrame maestro final listo para análisis
│
├── notebooks/                  # Jupyter Notebooks numerados lógicamente
│   ├── 01_data_ingestion_and_cleaning.ipynb
│   ├── 02_data_merging_and_master_creation.ipynb
│   ├── 03_EDA_sociodemografico.ipynb
│   ├── 04_EDA_sustancias_legales.ipynb
│   ├── 05_EDA_sustancias_ilegales_y_mercado.ipynb
│   └── 06_EDA_impacto_laboral_y_tratamiento.ipynb
│
├── src/                        # Scripts de Python con funciones auxiliares
│   ├── utils.py                # Funciones para cálculos ponderados y gráficos
│   └── diccionarios.py         # Mapeo de códigos a etiquetas legibles
│
├── outputs/                    # Resultados exportados
│   ├── figures/                # Gráficos en alta resolución para la tesis
│   └── tables/                 # Tablas resumen en formato CSV
│
├── docs/                       # Documentación del DANE
│   ├── Metodologia_ENCSPA.pdf
│   ├── Ficha_metodologica.pdf
│   ├── Manual_ENCSPA_2019_recoleccion_VF.pdf
│   └── Cuestionario_ENCSPA_2019.pdf
│
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Este archivo
```

## Requisitos del Sistema

### Entorno de Desarrollo
- Python 3.8 o superior
- Jupyter Notebook o JupyterLab
- Miniconda o Anaconda (recomendado)

### Instalación de Dependencias

```bash
# Crear y activar un entorno virtual con conda
conda create -n encspa python
conda activate encspa

# Instalar las dependencias
pip install -r requirements.txt
```

### Archivo `requirements.txt`

```
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
jupyter>=1.0.0
pyarrow>=10.0.0
fastparquet>=2022.0.0
openpyxl>=3.0.0
```

## Estructura de los Notebooks

### Notebook 01: Ingesta y Limpieza Inicial
**Archivo:** `01_data_ingestion_and_cleaning.ipynb`

- Carga todos los archivos CSV del DANE
- Estandarización de nombres de columnas (minúsculas, sin espacios)
- Eliminación de filas completamente nulas y duplicados
- Exportación a formato Parquet para mayor eficiencia

**Salida:** Archivos `.parquet` en `data/interim/`

---

### Notebook 02: Cruce de Datos y Creación del Maestro
**Archivo:** `02_data_merging_and_master_creation.ipynb`

- Cruce de tablas demográficas (`personas_seleccionadas`, `d_capitulos`, `d2_capitulos`)
- Left Joins con todos los módulos de sustancias (Capítulos E a S)
- Mapeo de variables clave (sexo, estado civil, nivel educativo)
- Creación de variables sintéticas (rangos de edad)

**Salida:** `df_master.parquet` en `data/processed/`

---

### Notebook 03: EDA Sociodemográfico
**Archivo:** `03_EDA_sociodemografico.ipynb`

**Análisis:**
- Distribución por sexo y rango de edad
- Nivel educativo de la población
- Salud mental: depresión por rango de edad

**Variables clave:** `sexo_desc`, `rango_edad`, `nivel_educativo`, `sentimiento_depresion`

**Gráficos generados:**
- `01_distribucion_rango_edad.png`
- `02_distribucion_nivel_educativo.png`
- `03_depresion_por_edad.png`

---

### Notebook 04: EDA Sustancias Legales
**Archivo:** `04_EDA_sustancias_legales.ipynb`

**Análisis:**
- Prevalencias de Tabaco y Alcohol (Vida, Año, Mes)
- Edad de inicio de consumo (KDE ponderado)
- Consumo de cigarrillos electrónicos vs. tabaco tradicional por edad
- Perfil de embriaguez en bebedores del último mes

**Variables clave:** `tabaco_vida`, `tabaco_12m`, `tabaco_30d`, `vapeador_vida`, `alcohol_vida`, `alcohol_12m`, `alcohol_30d`, `edad_inicio_tabaco`, `edad_inicio_alcohol`

**Gráficos generados:**
- `04_prevalencias_legales.png`
- `05_edad_inicio_legales.png`
- `06_vapeadores_vs_tabaco.png`
- `07_perfil_embriaguez.png`

---

### Notebook 05: EDA Sustancias Ilegales y Dinámicas de Mercado
**Archivo:** `05_EDA_sustancias_ilegales_y_mercado.ipynb`

**Análisis:**
- Prevalencias de Marihuana, Cocaína, Basuco y Éxtasis
- Perfil educativo por tipo de sustancia
- Canales de acceso al microtráfico (Olla, Domicilio, Redes Sociales, Amigos)
- Precios promedio del mercado ilegal

**Variables clave:** `marihuana_12m`, `cocaina_12m`, `basuco_12m`, `extasis_12m`, `nivel_educativo`, `k_10_*`, `l_09_*`, `n_10_*`, `precio_marihuana`, `precio_cocaina`, `precio_extasis`

**Gráficos generados:**
- `08_prevalencias_ilegales.png`
- `09_perfil_educativo_sustancias.png`
- `10_canales_microtrafico.png`

---

### Notebook 06: EDA Impacto Laboral, Tratamiento y Policonsumo
**Archivo:** `06_EDA_impacto_laboral_y_tratamiento.ipynb`

**Análisis:**
- Demanda de tratamiento por sustancia
- Impacto laboral: accidentes, ausentismo, bajo rendimiento
- Índice de policonsumo de sustancias ilegales
- Intersección entre policonsumo y resultados negativos

**Variables clave:** `tratamiento_necesidad_*`, `tratamiento_busqueda_ayuda`, `sustancia_principal_tratamiento`, `accidente_laboral`, `accidente_bajo_efecto`, `dias_ausentismo`, `ausentismo_por_sustancias`, `bajo_rendimiento_laboral`, `num_sustancias_ilegales`, `categoria_policonsumo`


## Diccionario de Variables Clave

### Identificadores (Para cruce de tablas)
| Variable | Descripción |
|----------|-------------|
| `directorio` | Identificador único del hogar |
| `secuencia_encuesta` | Número de hogar dentro de la vivienda |
| `secuencia_p` | Identificador de persona |
| `orden` | Orden de la persona dentro del hogar |

### Demográficas
| Variable | Descripción | Valores |
|----------|-------------|---------|
| `fex_c` | Factor de Expansión Final | Numérico (ponderación) |
| `sexo_desc` | Sexo de la persona | Hombre / Mujer |
| `edad` | Edad en años cumplidos | 12 - 65 |
| `rango_edad` | Rango etario | 12-17, 18-24, 25-34, 35-44, 45-54, 55-65 |
| `nivel_educativo` | Nivel educativo máximo alcanzado | Ninguno / Básica primaria / Básica secundaria / Media / Técnica / Universitaria / Postgrado |
| `estado_civil_desc` | Estado civil | Soltero / Casado / Viudo / Separado / Unión libre |

### Consumo de Sustancias
| Variable | Descripción | Valores |
|----------|-------------|---------|
| `tabaco_vida` | Consumo de tabaco alguna vez en la vida | 0/1 |
| `tabaco_12m` | Consumo de tabaco en últimos 12 meses | 0/1 |
| `alcohol_vida` | Consumo de alcohol alguna vez en la vida | 0/1 |
| `alcohol_12m` | Consumo de alcohol en últimos 12 meses | 0/1 |
| `marihuana_12m` | Consumo de marihuana en últimos 12 meses | 0/1 |
| `cocaina_12m` | Consumo de cocaína en últimos 12 meses | 0/1 |
| `basuco_12m` | Consumo de basuco en últimos 12 meses | 0/1 |
| `extasis_12m` | Consumo de éxtasis en últimos 12 meses | 0/1 |
| `num_sustancias_ilegales` | Número de sustancias ilegales consumidas | 0 - 4 |
| `categoria_policonsumo` | Categoría de policonsumo | 0 sustancias / 1 sustancia / 2 sustancias / 3+ sustancias |

## Metodología de Análisis

### Factor de Expansión
Todos los análisis utilizan la variable `fex_c` (Factor de Expansión Final) para ponderar las estimaciones. Esto significa que los resultados representan a la población colombiana de 12 a 65 años, no solo a la muestra encuestada.

### Prevalencias
- **Prevalencia de Vida:** Personas que han consumido la sustancia alguna vez
- **Prevalencia de Año:** Personas que consumieron en los últimos 12 meses
- **Prevalencia de Mes:** Personas que consumieron en los últimos 30 días

### Policonsumo
Se define como el consumo de dos o más sustancias ilegales diferentes en los últimos 12 meses. Se utiliza como indicador de mayor riesgo.

## Fuentes de Datos

Los datos provienen de la **Encuesta Nacional de Consumo de Sustancias Psicoactivas en Población General (ENCSPA) 2019**, disponible en el catálogo de microdatos del DANE:

- **URL:** http://microdatos.dane.gov.co/index.php
- **ID del Documento:** COL-DANE-ENSCPA-2019


## Licencia

Este proyecto es de uso académico. Los datos son propiedad del DANE y su uso está sujeto a las condiciones establecidas en el catálogo de microdatos.