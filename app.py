import streamlit as st
import pandas as pd
import plotly_express as px

# 1. Cargar el conjunto de datos
try:
    car_data = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("Error: El archivo vehicles_us.csv no se encontró.")
    st.error("Asegúrate de que el archivo esté en la misma carpeta que app.py")
    st.stop() # Detiene la ejecución de la aplicación si el archivo no se encuentra

# 2. Limpieza y Preprocesamiento de Datos (replicando pasos del EDA)
# Aquí aplicamos las mismas lógicas de limpieza que en el Jupyter Notebook

# Imputar 'is_4wd': Rellenar NaN con 0 y convertir a int
car_data['is_4wd'] = car_data['is_4wd'].fillna(0).astype(int)

# Imputar 'paint_color': Rellenar NaN con 'unknown' y convertir a category
car_data['paint_color'] = car_data['paint_color'].fillna('unknown').astype('category')

# Imputar 'odometer': Rellenar NaN con la mediana y convertir a int
median_odometer = car_data['odometer'].median()
car_data['odometer'] = car_data['odometer'].fillna(median_odometer).astype(int)

# Imputar 'cylinders': Rellenar NaN con la mediana y convertir a int
median_cylinders = car_data['cylinders'].median()
car_data['cylinders'] = car_data['cylinders'].fillna(median_cylinders).astype(int)

# Imputar 'model_year': Rellenar NaN con la mediana y convertir a int
median_model_year = car_data['model_year'].median()
car_data['model_year'] = car_data['model_year'].fillna(median_model_year).astype(int)

# Convertir 'date_posted' a tipo datetime
car_data['date_posted'] = pd.to_datetime(car_data['date_posted'])

# Convertir columnas categóricas a tipo 'category' para optimizar memoria
categorical_cols = ['model', 'condition', 'fuel', 'transmission', 'type']
for col in categorical_cols:
    car_data[col] = car_data[col].astype('category')

# 3. Configurar el encabezado de la aplicación
st.header('Análisis de Anuncios de Venta de Vehículos')

# 4. Crear la barra lateral con filtros
st.sidebar.header('Filtros de Datos')

# Filtro por Año del Modelo
min_year, max_year = int(car_data['model_year'].min()), int(car_data['model_year'].max())
selected_year_range = st.sidebar.slider(
    'Selecciona el Año del Modelo',
    min_year, max_year, (min_year, max_year)
)

# Filtro por Rango de Precios
min_price, max_price = int(car_data['price'].min()), int(car_data['price'].max())
selected_price_range = st.sidebar.slider(
    'Selecciona el Rango de Precios ($)',
    min_price, max_price, (min_price, max_price)
)

# Filtro por Kilometraje
min_odometer, max_odometer = int(car_data['odometer'].min()), int(car_data['odometer'].max())
selected_odometer_range = st.sidebar.slider(
    'Selecciona el Rango de Kilometraje',
    min_odometer, max_odometer, (min_odometer, max_odometer)
)

# Filtro por Condición
unique_conditions = car_data['condition'].unique().tolist()
selected_conditions = st.sidebar.multiselect(
    'Selecciona la Condición del Vehículo',
    unique_conditions,
    default=[] # Lista vacía para no seleccionar todas por defecto
)

if not selected_conditions:
    selected_conditions = unique_conditions # Si no se selecciona nada, muestra todas las condiciones

# Filtro por Tipo de Vehículo
unique_types = car_data['type'].unique().tolist()
selected_types = st.sidebar.multiselect(
    'Selecciona el Tipo de Vehículo',
    unique_types,
    default=[] # Lista vacía para no seleccionar todas por defecto
)

if not selected_types:
    selected_types = unique_types # Si no se selecciona nada, muestra todos los tipos

# Aplicar los filtros al DataFrame
filtered_car_data = car_data[
    (car_data['model_year'].between(selected_year_range[0], selected_year_range[1])) &
    (car_data['price'].between(selected_price_range[0], selected_price_range[1])) &
    (car_data['odometer'].between(selected_odometer_range[0], selected_odometer_range[1])) &
    (car_data['condition'].isin(selected_conditions)) &
    (car_data['type'].isin(selected_types))
]

st.write(f"Mostrando {len(filtered_car_data)} de {len(car_data)} anuncios después de aplicar filtros.")
st.write("---") # Separador visual

# 5. Crear casillas de verificación para seleccionar los gráficos
st.write("Selecciona los gráficos que deseas visualizar:")

# Casilla de verificación para el histograma de kilometraje
build_histogram = st.checkbox('Construir Histograma de Kilometraje')

# Casilla de verificación para el gráfico de dispersión (precio vs. kilometraje)
build_scatter_odometer = st.checkbox('Construir Gráfico de Dispersión: Precio vs. Kilometraje')

# Casilla de verificación para el gráfico de dispersión (precio vs. año del modelo)
build_scatter_year = st.checkbox('Construir Gráfico de Dispersión: Precio vs. Año del Modelo')

# 6. Lógica para mostrar los gráficos basados en las casillas de verificación
# Ahora los gráficos usan 'filtered_car_data'
if build_histogram:
    st.write('Creando un histograma para el conjunto de datos de anuncios de venta de coches (Kilometraje)')

    # Crear el histograma de 'odometer' (kilometraje)
    fig_hist = px.histogram(filtered_car_data, x="odometer", title="Distribución de Kilometraje (Odometer)",
                            labels={"odometer": "Kilometraje (millas/km)", "count": "Cantidad de Vehículos"},
                            nbins=50) # Puedes ajustar el número de bins

    # Mostrar el gráfico Plotly interactivo en Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter_odometer:
    st.write('Creando un gráfico de dispersión: Precio vs. Kilometraje')

    # Crear el gráfico de dispersión de precio vs. kilometraje
    fig_scatter_odometer = px.scatter(filtered_car_data, x="odometer", y="price",
                                      title="Precio vs. Kilometraje (Odometer)",
                                      labels={"odometer": "Kilometraje (millas/km)", "price": "Precio ($)"},
                                      hover_data=['model', 'model_year', 'condition']) # Muestra info al pasar el ratón

    # Mostrar el gráfico Plotly interactivo en Streamlit
    st.plotly_chart(fig_scatter_odometer, use_container_width=True)

if build_scatter_year:
    st.write('Creando un gráfico de dispersión: Precio vs. Año del Modelo')

    # Crear el gráfico de dispersión de precio vs. año del modelo
    fig_scatter_year = px.scatter(filtered_car_data, x="model_year", y="price",
                                   title="Precio vs. Año del Modelo",
                                   labels={"model_year": "Año del Modelo", "price": "Precio ($)"},
                                   hover_data=['model', 'odometer', 'condition']) # Muestra info al pasar el ratón

    # Mostrar el gráfico Plotly interactivo en Streamlit
    st.plotly_chart(fig_scatter_year, use_container_width=True)