# 🎵 Dashboard de Comportamiento de Usuarios Spotify

Un dashboard interactivo creado con Streamlit para analizar y visualizar el comportamiento de usuarios de Spotify basado en datos reales de 50,000 usuarios.

## 📊 Características Principales

### Métricas KPI
- Usuarios activos vs inactivos
- Edad promedio de los usuarios
- Horas de escucha promedio por semana
- Número promedio de playlists creadas
- Calificación promedio de sugerencias musicales

### Visualizaciones Interactivas
- **Distribución de tipos de suscripción** (Premium Individual, Family, Duo, Student, Free)
- **Estado de suscripción** (Activos vs Inactivos)
- **Distribución demográfica** por edad
- **Análisis de comportamiento** de escucha
- **Top géneros musicales** favoritos
- **Dispositivos principales** utilizados
- **Interacción con anuncios** y conversión
- **Calificaciones de sugerencias** musicales
- **Características más valoradas** por los usuarios
- **Análisis de países** con más usuarios
- **Patrones de inactividad** por meses

### Filtros Interactivos
- Filtrado por país
- Filtrado por tipo de suscripción
- Rango de edad ajustable
- Filtrado por estado de suscripción en la tabla de datos

## 🚀 Instalación y Ejecución

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clona o descarga el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd spotify-dashboard
   ```

2. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta el dashboard**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Accede al dashboard**
   - Abre tu navegador web en: `http://localhost:8501`

## 📁 Estructura del Proyecto

```
spotify-dashboard/
│
├── streamlit_app.py              # Aplicación principal del dashboard
├── spotify_user_behavior_realistic_50000_rows.csv  # Dataset de usuarios
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Documentación del proyecto
```

## 📊 Dataset

El dataset contiene información de 50,000 usuarios de Spotify con las siguientes variables:

- **id_usuario**: Identificador único del usuario
- **pais**: País de residencia
- **edad**: Edad del usuario
- **fecha_registro**: Fecha de registro en la plataforma
- **tipo_suscripcion**: Tipo de plan (Free, Premium Individual, Family, Duo, Student)
- **estado_suscripcion**: Estado actual (Active/Inactive)
- **meses_inactivo**: Número de meses sin actividad
- **bandera_inactivo_3_meses**: Indicador de inactividad > 3 meses
- **interaccion_anuncio**: Si interactúa con anuncios (Yes/No)
- **conversion_anuncio_a_suscripcion**: Si se convirtió por anuncios
- **calificacion_sugerencia_musica_1_a_5**: Calificación de sugerencias (1-5)
- **horas_escucha_promedio_por_semana**: Horas de escucha semanales
- **genero_favorito**: Género musical preferido
- **caracteristica_mas_gustada**: Feature más valorada
- **caracteristica_futura_deseada**: Feature deseada para el futuro
- **dispositivo_principal**: Dispositivo principal de uso
- **playlists_creadas**: Número de playlists creadas
- **saltos_promedio_por_dia**: Promedio de saltos diarios

## 🛠️ Tecnologías Utilizadas

- **Streamlit**: Framework para aplicaciones web de datos
- **Pandas**: Manipulación y análisis de datos
- **Plotly**: Gráficos interactivos
- **Matplotlib/Seaborn**: Visualizaciones adicionales
- **Python**: Lenguaje de programación principal

## 📈 Funcionalidades

### Dashboard Interactivo
- **Filtros en tiempo real**: Los gráficos se actualizan automáticamente según los filtros aplicados
- **Métricas dinámicas**: Los KPIs se recalculan basándose en los datos filtrados
- **Visualizaciones responsivas**: Gráficos que se adaptan al tamaño de la pantalla

### Análisis de Datos
- **Limpieza automática**: El código incluye funciones para limpiar y preparar los datos
- **Cálculos estadísticos**: Promedios, distribuciones y correlaciones
- **Agrupaciones inteligentes**: Análisis por categorías relevantes

## 🤝 Contribución

Si deseas contribuir al proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Contacto

Para preguntas o sugerencias, por favor abre un issue en el repositorio.

---

**Desarrollado con ❤️ para análisis de datos de Spotify**
