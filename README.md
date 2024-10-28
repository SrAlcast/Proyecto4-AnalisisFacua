# 🛒 Proyecto 4: Análisis de Precios de Supermercados (FACUA)

![Logo FACUA](https://raw.githubusercontent.com/SrAlcast/Proyecto4-AnalisisFacua/a4e8e424f36ed1133c5f2b909ce110d6d9a73170/src/LOGO%20FACUA.jpg)

## 📋 Descripción General

Este proyecto tiene como objetivo recolectar, procesar y analizar datos sobre los precios de productos en distintos supermercados de España. Utiliza técnicas de scraping, bases de datos SQL, y análisis exploratorio para extraer información relevante sobre la variabilidad de precios y otras tendencias. La fuente principal de datos es la página web [FACUA: Precios Supermercados](https://super.facua.org/).

## 🎯 Objetivos Específicos
- **🔍 Scraping de datos**: Extraer datos de precios de productos básicos de seis supermercados principales en España: Alcampo, Carrefour, Dia, Eroski, Hipercor y Mercadona.
- **💾 Almacenamiento en SQL**: Crear y poblar una base de datos SQL que permita almacenar y consultar la información recolectada.
- **📊 Análisis Exploratorio de Datos**: Examinar la distribución y variabilidad de los precios por supermercado y producto.
- **📈 Visualización de Resultados**: Crear gráficos que faciliten la interpretación de tendencias y patrones en los precios.

## 📁 Estructura del Proyecto

```bash
├── data/                  # CSVs de extracción
├── notebooks/             # Jupyter Notebooks con el codigo de scraping y creacion de BBDD
├── results/               # Jupyter Notebooks con el codigo de visualizaciones y scrip de consultas
├── src/                   # Código fuente principal y los módulos de la aplicación
├── README.md              # Descripción del proyecto (este archivo)
```

## ⚙️ Requisitos

1. **Python 3.x**
2. **Bibliotecas necesarias**:
   - `requests`
   - `beautifulsoup4`
   - `pandas`
   - `sqlalchemy`
   - `matplotlib`
   - `seaborn`

Para instalarlas, puedes usar:
```bash
pip install requests beautifulsoup4 pandas sqlalchemy matplotlib seaborn
```

## 🚀 Uso del Proyecto

1. **Realizar el Scraping**:
   Ejecuta el script de scraping en la carpeta `notebooks/` para recolectar datos de la página de FACUA.

2. **Poblar la Base de Datos SQL**:
   Usa los datos recolectados para llenar la base de datos SQL. El script de creación de la base de datos está en la carpeta `notebooks/`.

3. **Análisis y Visualización**:
   Abre los notebooks en `results/` para realizar análisis exploratorios y visualizar los resultados.

## 📊 Resultados

El análisis permite observar cómo los precios varían entre supermercados y proporciona insights sobre tendencias, como el impacto de la ubicación geográfica en los precios o la estacionalidad de ciertos productos.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue el formato de GitHub Flow para colaborar y asegúrate de documentar bien cualquier cambio.

 
