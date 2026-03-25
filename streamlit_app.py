import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd # Import pandas for direct CSV reading
import os

# Define the base path for the Kaggle dataset in Colab
kaggle_dataset_path = "/kaggle/input/spotify-user-behavior-and-pattern"
file_name = "spotify_user_behavior_realistic_50000_rows.csv" # Corrected file name
full_file_path = os.path.join(kaggle_dataset_path, file_name)

# List files in the dataset directory to verify the file name
print(f"Files in {kaggle_dataset_path}:")
for root, dirs, files in os.walk(kaggle_dataset_path):
    for f in files:
        print(os.path.join(root, f))

# Load the dataset directly using pandas from the mounted path
try:
    df = pd.read_csv(full_file_path)
    print("Dataset loaded successfully using pandas.")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found at '{kaggle_dataset_path}'. Please check the filename or path.")
    df = pd.DataFrame() # Initialize an empty DataFrame to avoid further errors
except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")
    df = pd.DataFrame() # Initialize an empty DataFrame on other errors


print("First 5 records:", df.head())

if not df.empty:
    print("Iniciando limpieza del dataset...")

    # Renombrar las columnas a español y en formato snake_case
    column_mapping = {
        'user_id': 'id_usuario',
        'country': 'pais',
        'age': 'edad',
        'signup_date': 'fecha_registro',
        'subscription_type': 'tipo_suscripcion',
        'subscription_status': 'estado_suscripcion',
        'months_inactive': 'meses_inactivo',
        'inactive_3_months_flag': 'bandera_inactivo_3_meses',
        'ad_interaction': 'interaccion_anuncio',
        'ad_conversion_to_subscription': 'conversion_anuncio_a_suscripcion',
        'music_suggestion_rating_1_to_5': 'calificacion_sugerencia_musica_1_a_5',
        'avg_listening_hours_per_week': 'horas_escucha_promedio_por_semana',
        'favorite_genre': 'genero_favorito',
        'most_liked_feature': 'caracteristica_mas_gustada',
        'desired_future_feature': 'caracteristica_futura_deseada',
        'primary_device': 'dispositivo_principal',
        'playlists_created': 'playlists_creadas',
        'avg_skips_per_day': 'saltos_promedio_por_dia'
    }
    df.rename(columns=column_mapping, inplace=True)
    print("Columnas renombradas exitosamente.")

    # 1. Rellenar valores nulos con la media para 'horas_escucha_promedio_por_semana'
    for col in ['horas_escucha_promedio_por_semana']:
        if col in df.columns and df[col].isnull().any():
            mean_val = df[col].mean()
            df[col].fillna(mean_val, inplace=True)
            print(f"Valores nulos en '{col}' rellenados con la media: {mean_val:.2f}")
        elif col not in df.columns:
            print(f"Advertencia: La columna '{col}' no se encontró en el DataFrame.")

    # 2. La columna 'fecha_registro' ya está en formato fecha (datetime64[ns]) y sin nulos.
    print("Columna 'fecha_registro' ya está en formato fecha.")

    # 3. Crear una nueva columna 'User_LTV'
    # Las columnas 'meses_suscripcion' y 'precio_plan' no se encontraron en el DataFrame.
    if 'meses_suscripcion' in df.columns and 'precio_plan' in df.columns:
        df['User_LTV'] = df['meses_suscripcion'] * df['precio_plan']
        print("Columna 'User_LTV' creada exitosamente.")
    else:
        print("Advertencia: No se pudieron crear 'User_LTV'. Las columnas 'meses_suscripcion' y/o 'precio_plan' no se encontraron en el DataFrame.")

    # 4. Eliminar filas donde el 'id_usuario' esté duplicado
    if 'id_usuario' in df.columns:
        initial_rows = df.shape[0]
        df.drop_duplicates(subset=['id_usuario'], inplace=True)
        rows_after_dropping = df.shape[0]
        if initial_rows > rows_after_dropping:
            print(f"Se eliminaron {initial_rows - rows_after_dropping} filas duplicadas basadas en 'id_usuario'.")
            print(f"Filas restantes en el DataFrame: {rows_after_dropping}")
        else:
            print("No se encontraron 'id_usuario' duplicados.")
    else:
        print("Advertencia: La columna 'id_usuario' no se encontró en el DataFrame. No se eliminaron duplicados.")

    print("Limpieza del dataset finalizada.")
    # display(df.head()) # Removido para mantener la salida concisa en este paso de preparación
    # display(df.info()) # Removido para mantener la salida concisa en este paso de preparación
else:
    print("El DataFrame está vacío, no se puede realizar la limpieza.")
if not df.empty:
    display(df.head())
else:
    print("No se pueden mostrar las primeras filas, el DataFrame está vacío (posiblemente porque 'datos.csv' no fue encontrado).")
import matplotlib.pyplot as plt
import seaborn as sns

# Establecer un estilo visual profesional
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

if not df.empty:
    subscription_counts = df['tipo_suscripcion'].value_counts()
    plt.figure(figsize=(9, 9))
    plt.pie(subscription_counts, labels=subscription_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("viridis", len(subscription_counts)))
    plt.title('Distribución de Tipos de Suscripción')
    plt.axis('equal') # Para asegurar que el pastel sea un círculo.
    plt.tight_layout()
    plt.show()
else:
    print("El DataFrame está vacío, no se puede generar el gráfico de pastel de suscripciones.")
if not df.empty:
    # Para este análisis, podemos ver la relación entre horas de escucha y si están inactivos
    # Convertiremos 'bandera_inactivo_3_meses' a una etiqueta para el gráfico.
    df['estado_churn'] = df['bandera_inactivo_3_meses'].apply(lambda x: 'Inactivo (+3 meses)' if x == 1 else 'Activo / Inactivo (<3 meses)')

    plt.figure(figsize=(12, 7))
    sns.scatterplot(
        data=df,
        x='horas_escucha_promedio_por_semana',
        y='meses_inactivo',
        hue='estado_churn', # Usamos la nueva columna para diferenciar por color
        palette={'Activo / Inactivo (<3 meses)': 'green', 'Inactivo (+3 meses)': 'red'},
        alpha=0.6,
        s=50 # Tamaño de los puntos
    )
    plt.title('Horas de Escucha vs Meses de Inactividad por Estado de Churn')
    plt.xlabel('Horas de Escucha Promedio por Semana')
    plt.ylabel('Meses Inactivo')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # Eliminamos la columna temporal
    df.drop(columns=['estado_churn'], inplace=True)
else:
    print("El DataFrame está vacío, no se puede generar el gráfico de dispersión.")
if not df.empty:
    # Asumimos que 'meses_inactivo' puede indicar el momento del churn
    # Si 'meses_inactivo' es > 0, el usuario está inactivo.
    churned_users = df[df['meses_inactivo'] > 0]

    if not churned_users.empty:
        plt.figure(figsize=(10, 6))
        sns.histplot(churned_users['meses_inactivo'], bins=range(1, int(churned_users['meses_inactivo'].max()) + 2), kde=False, color='darkorange')
        plt.title('Distribución de Meses Inactivo (para Usuarios Inactivos)')
        plt.xlabel('Meses Inactivo (aproximación del mes de abandono)')
        plt.ylabel('Número de Usuarios')
        plt.xticks(range(1, int(churned_users['meses_inactivo'].max()) + 1))
        plt.tight_layout()
        plt.show()
    else:
        print("No hay usuarios inactivos para analizar el patrón de abandono por meses.")
else:
    print("El DataFrame está vacío, no se puede generar el histograma de churn.")
if not df.empty:
    # Asumimos que 'meses_inactivo' puede indicar el momento del churn
    # Si 'meses_inactivo' es > 0, el usuario está inactivo.
    churned_users = df[df['meses_inactivo'] > 0]

    if not churned_users.empty:
        plt.figure(figsize=(10, 6))
        sns.histplot(churned_users['meses_inactivo'], bins=range(1, int(churned_users['meses_inactivo'].max()) + 2), kde=False, color='darkorange')
        plt.title('Distribución de Meses Inactivo (para Usuarios Inactivos)')
        plt.xlabel('Meses Inactivo (aproximación del mes de abandono)')
        plt.ylabel('Número de Usuarios')
        plt.xticks(range(1, int(churned_users['meses_inactivo'].max()) + 1))
        plt.tight_layout()
        plt.show()
    else:
        print("No hay usuarios inactivos para analizar el patrón de abandono por meses.")
else:
    print("El DataFrame está vacío, no se puede generar el histograma de churn.")
