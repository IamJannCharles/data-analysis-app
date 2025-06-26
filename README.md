
# 🚗 Análisis Exploratorio de Datos (EDA) y Aplicación Web de Anuncios de Vehículos

¡Bienvenido al proyecto de Análisis Exploratorio de Datos de Anuncios de Vehículos!  
Este repositorio contiene un proyecto de ciencia de datos que realiza un análisis detallado de un conjunto de anuncios de venta de vehículos y presenta los hallazgos a través de una **aplicación web interactiva** desarrollada con **Streamlit**.

---

## 🌐 Demostración en Vivo

Puedes probar la aplicación web directamente desde aquí:

👉 [**Abrir la aplicación en Render**](https://data-analysis-app-paiq.onrender.com)

---

## 📊 Descripción del Proyecto

El objetivo principal es explorar el conjunto de datos `vehicles_us.csv` para comprender patrones y relaciones entre las diferentes características de los vehículos.  
Luego, se ha desarrollado una aplicación web con Streamlit para visualizar esos datos de forma interactiva.

---

## 📁 Contenido del Proyecto

- `notebooks/EDA.ipynb`: Análisis exploratorio de datos (EDA): limpieza, estadísticos y visualizaciones.  
- `app.py`: Aplicación web construida con Streamlit.  
- `requirements.txt`: Dependencias necesarias para ejecutar el proyecto.  

---

## 🧠 Características de la Aplicación Web

### ✅ Carga y Preprocesamiento de Datos
- Carga automática del dataset.  
- Limpieza y transformación de tipos de datos según lo definido en el EDA.

### 🎛️ Filtros Interactivos (en `st.sidebar`)
- Rango de **Año del Modelo**  
- Rango de **Precios**  
- Rango de **Kilometraje**  
- Filtro múltiple de **Condición del Vehículo**  
- Filtro múltiple de **Tipo de Vehículo**

### 📈 Visualizaciones Dinámicas
Seleccionables por el usuario:
- Histograma de **Kilometraje**  
- Dispersión: **Precio vs. Kilometraje**  
- Dispersión: **Precio vs. Año del Modelo**

---

## ⚙️ Configuración y Ejecución Local

### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/IamJannCharles/data-analysis-app.git
cd data-analysis-app
```

### 2️⃣ Crear y Activar un Entorno Virtual

```bash
# Crear entorno virtual
python -m venv vehicles_env

# Activar entorno virtual
# En Windows:
.\vehicles_env\Scripts\activate

# En macOS/Linux:
source vehicles_env/bin/activate
```

### 3️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Descargar el Conjunto de Datos

[Descarga](https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv) el archivo `vehicles_us.csv` y colócalo en la **raíz del proyecto**, junto a `app.py` y `README.md`.

### 5️⃣ Ejecutar la Aplicación Streamlit

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador predeterminado.

---

## 📓 Exploración con Jupyter Notebook

Para revisar el análisis exploratorio en profundidad:

1. Abre `notebooks/EDA.ipynb` en VS Code o Jupyter.  
2. Asegúrate de que el intérprete sea el del entorno `vehicles_env`.

---

## 📬 Contacto

Si tienes alguna pregunta, sugerencia o quieres contribuir, no dudes en abrir un [issue](https://github.com/IamJannCharles/data-analysis-app/issues).

---

**Autor:** Jann Charles  
**Licencia:** MIT
