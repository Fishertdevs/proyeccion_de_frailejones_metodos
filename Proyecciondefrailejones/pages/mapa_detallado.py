
import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap, MarkerCluster
from streamlit_folium import st_folium
from data.regions import get_frailejon_regions

st.set_page_config(
    page_title="Mapa Detallado - Impacto de Frailejones en Colombia",
    page_icon="🌿",
    layout="wide"
)

# Estilo para mantener consistencia con la página principal
st.markdown("""
<style>
    .main {
        background-color: #f8fffe;
    }
    .main-header {
        font-size: 2.5rem;
        color: #2d5016;
        text-align: center;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #4a7c2a;
        font-weight: 600;
    }
    .description {
        font-size: 1rem;
        line-height: 1.5;
        color: #2c5530;
    }
    .highlight {
        background-color: #4caf50;
        color: white;
        padding: 0.2rem;
        border-radius: 0.2rem;
    }
    .card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.15);
        margin-bottom: 1rem;
        border: 1px solid #c8e6c9;
    }
    .map-container {
        border: 2px solid #4caf50;
        border-radius: 1rem;
        padding: 10px;
        margin-bottom: 1rem;
        background-color: #f1f8e9;
    }
    /* Ajustes para el contraste de texto */
    h1, h2, h3, h4, h5, h6 {
        color: #2d5016 !important;
    }
    p, li, span {
        color: #2c5530 !important;
    }
    
    .stButton button {
        background-color: #4caf50 !important;
        color: white !important;
        border: none !important;
        border-radius: 0.5rem !important;
        padding: 0.5rem 1rem !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h1 class='main-header'>🌿 Mapa de Páramos y Frailejones en Colombia</h1>", unsafe_allow_html=True)

# Contenido principal
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-header'>Análisis de Ecosistemas de Páramo por Región</h2>", unsafe_allow_html=True)
st.markdown("""
<p class='description'>
Este mapa detallado muestra los páramos de Colombia y las regiones más vulnerables a la pérdida de frailejones. 
Puede explorar diferentes visualizaciones y filtrar por nivel de riesgo o densidad de frailejones en cada páramo.
Los frailejones son fundamentales para la regulación hídrica y la conservación de la biodiversidad en los ecosistemas de alta montaña.
</p>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Controles
control_col1, control_col2, control_col3 = st.columns(3)
with control_col1:
    map_type = st.selectbox(
        "Tipo de visualización",
        ["Marcadores de Páramos", "Densidad de Frailejones", "Clusters por Región"],
        index=0
    )

with control_col2:
    risk_filter = st.multiselect(
        "Filtrar por nivel de riesgo",
        ["Crítico", "Alto", "Medio", "Bajo"],
        default=["Crítico", "Alto", "Medio", "Bajo"]
    )

with control_col3:
    frailejon_threshold = st.slider(
        "Densidad mínima de frailejones (%)",
        min_value=0,
        max_value=100,
        value=20,
        step=5
    )

# Crear el mapa
st.markdown("<div class='map-container'>", unsafe_allow_html=True)

# Obtener datos de páramos
paramos = get_frailejon_regions()

# Filtrar datos según selecciones
filtered_paramos = [
    paramo for paramo in paramos
    if paramo["risk"] in risk_filter and paramo["frailejon_density"] >= frailejon_threshold
]

# Crear mapa base centrado en los páramos colombianos
m = folium.Map(location=[5.5, -73.5], zoom_start=6, tiles='CartoDB positron')

# Agregar visualización según selección
if map_type == "Marcadores de Páramos":
    for paramo in filtered_paramos:
        # Determinar color basado en riesgo
        if paramo["risk"] == "Crítico":
            color = 'darkred'
        elif paramo["risk"] == "Alto":
            color = 'red'
        elif paramo["risk"] == "Medio":
            color = 'orange'
        else:
            color = 'green'
            
        # Crear popup con información
        popup_content = f"""
        <div style="width: 280px">
            <h4>{paramo['name']}</h4>
            <p><strong>Nivel de riesgo:</strong> {paramo['risk']}</p>
            <p><strong>Densidad de frailejones:</strong> {paramo['frailejon_density']}%</p>
            <p><strong>Área aproximada:</strong> {paramo['area']} km²</p>
            <p><strong>Altitud promedio:</strong> {paramo['altitude']} msnm</p>
            <p><strong>Servicios ecosistémicos:</strong> {paramo['ecosystem_services']}</p>
            <p><strong>Estado:</strong> {paramo['description']}</p>
        </div>
        """
        tooltip = f"{paramo['name']} - Riesgo: {paramo['risk']}"
        
        # Añadir marcador
        folium.Marker(
            location=[paramo['lat'], paramo['lon']],
            popup=folium.Popup(popup_content, max_width=320),
            tooltip=tooltip,
            icon=folium.Icon(color=color, icon='tree', prefix='fa')
        ).add_to(m)
        
        # Círculo con tamaño proporcional a la densidad de frailejones
        folium.Circle(
            radius=paramo['frailejon_density'] * 800,
            location=[paramo['lat'], paramo['lon']],
            color=color,
            fill=True,
            fill_opacity=0.3,
            opacity=0.7,
            weight=2
        ).add_to(m)

elif map_type == "Densidad de Frailejones":
    # Datos para el mapa de calor
    heat_data = [[paramo['lat'], paramo['lon'], paramo['frailejon_density']] for paramo in filtered_paramos]
    
    # Añadir mapa de calor
    HeatMap(
        heat_data,
        radius=20,
        min_opacity=0.4,
        gradient={
            0.4: '#81c784',
            0.6: '#66bb6a',
            0.8: '#4caf50',
            1.0: '#2e7d32'
        },
        blur=15
    ).add_to(m)

elif map_type == "Clusters por Región":
    # Crear clúster de marcadores
    marker_cluster = MarkerCluster().add_to(m)
    
    for paramo in filtered_paramos:
        # Determinar color basado en riesgo
        if paramo["risk"] == "Crítico":
            color = 'darkred'
        elif paramo["risk"] == "Alto":
            color = 'red'
        elif paramo["risk"] == "Medio":
            color = 'orange'
        else:
            color = 'green'
            
        # Crear popup con información
        popup_content = f"""
        <div style="width: 280px">
            <h4>{paramo['name']}</h4>
            <p><strong>Nivel de riesgo:</strong> {paramo['risk']}</p>
            <p><strong>Densidad de frailejones:</strong> {paramo['frailejon_density']}%</p>
            <p><strong>Área:</strong> {paramo['area']} km²</p>
            <p><strong>Altitud:</strong> {paramo['altitude']} msnm</p>
        </div>
        """
        
        # Añadir marcador al clúster
        folium.Marker(
            location=[paramo['lat'], paramo['lon']],
            popup=folium.Popup(popup_content, max_width=320),
            tooltip=paramo['name'],
            icon=folium.Icon(color=color, icon='tree', prefix='fa')
        ).add_to(marker_cluster)

# Mostrar el mapa
st_folium(m, width=1200, height=600)
st.markdown("</div>", unsafe_allow_html=True)

# Análisis adicional
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-header'>Análisis de Páramos por Región</h2>", unsafe_allow_html=True)

# Crear dataframe para análisis
paramo_df = pd.DataFrame([
    {
        'Páramo': paramo['name'],
        'Departamento': paramo.get('department', 'N/A'),
        'Riesgo': paramo['risk'],
        'Densidad Frailejones (%)': paramo['frailejon_density'],
        'Área (km²)': paramo['area'],
        'Altitud (msnm)': paramo['altitude']
    }
    for paramo in paramos
])

# Mostrar estadísticas
analysis_col1, analysis_col2 = st.columns(2)

with analysis_col1:
    st.subheader("Páramos por nivel de riesgo")
    risk_counts = paramo_df['Riesgo'].value_counts()
    st.bar_chart(risk_counts)

with analysis_col2:
    st.subheader("Densidad promedio de frailejones por riesgo")
    avg_density = paramo_df.groupby('Riesgo')['Densidad Frailejones (%)'].mean().sort_values(ascending=False)
    st.bar_chart(avg_density)

# Métricas importantes
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    total_paramos = len(paramos)
    st.metric("Total de Páramos", total_paramos)

with metric_col2:
    critical_paramos = len([p for p in paramos if p['risk'] == 'Crítico'])
    st.metric("Páramos en Riesgo Crítico", critical_paramos, delta=f"{critical_paramos/total_paramos*100:.1f}%")

with metric_col3:
    avg_density = sum(p['frailejon_density'] for p in paramos) / len(paramos)
    st.metric("Densidad Promedio", f"{avg_density:.1f}%")

with metric_col4:
    total_area = sum(p['area'] for p in paramos)
    st.metric("Área Total de Páramos", f"{total_area:,} km²")

# Tabla de datos
st.subheader("Datos detallados por páramo")
st.dataframe(paramo_df, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# Conclusiones y recomendaciones
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-header'>Conclusiones y Recomendaciones para la Conservación</h2>", unsafe_allow_html=True)
st.markdown("""
<p class='description'>
El análisis del mapa de páramos muestra que las regiones con mayor vulnerabilidad a la pérdida de frailejones
se concentran en zonas de alta montaña con presión antrópica, principalmente:
</p>

<ul>
    <li><strong>Páramo de Santurbán (Santander):</strong> Alta presión por actividades mineras y agrícolas</li>
    <li><strong>Páramo de Sumapaz (Cundinamarca/Meta):</strong> El páramo más grande del mundo, fundamental para Bogotá</li>
    <li><strong>Páramo de Chingaza (Cundinamarca/Meta):</strong> Principal fuente de agua para la región capital</li>
    <li><strong>Páramo de Guerrero (Cundinamarca):</strong> Presión por expansión urbana y agricultura</li>
</ul>

<p class='description'>
Se recomienda implementar estrategias de conservación focalizadas en estos páramos, incluyendo:
</p>

<ol>
    <li><strong>Restauración ecológica:</strong> Programas de siembra de frailejones nativos en áreas degradadas</li>
    <li><strong>Monitoreo continuo:</strong> Sistemas de seguimiento de poblaciones de frailejones y calidad del agua</li>
    <li><strong>Educación ambiental:</strong> Sensibilización sobre la importancia de los frailejones para el abastecimiento hídrico</li>
    <li><strong>Regulación de actividades:</strong> Control estricto de minería, agricultura y ganadería en zonas de páramo</li>
    <li><strong>Conectividad ecológica:</strong> Corredores biológicos entre páramos para facilitar la dispersión de especies</li>
    <li><strong>Investigación científica:</strong> Estudios sobre adaptación al cambio climático y técnicas de propagación</li>
</ol>

<div class='highlight'>
<p><strong>Dato importante:</strong> Los frailejones crecen solo 1-2 cm por año y pueden vivir hasta 150 años. 
Su recuperación natural es extremadamente lenta, por lo que la conservación preventiva es fundamental.</p>
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="background: linear-gradient(135deg, #4caf50 0%, #66bb6a 100%); color: white; text-align: center; padding: 15px; border-radius: 10px; margin-top: 20px;">
<h4 style="color: white !important; margin: 0;">🌿 Conservación de Frailejones en Colombia | Universidad Central 2025</h4>
<p style="color: white !important; margin: 5px 0 0 0; font-size: 0.9rem;">Proyecto de Métodos Numéricos - Simulación de Ecosistemas de Páramo</p>
</div>
""", unsafe_allow_html=True)
