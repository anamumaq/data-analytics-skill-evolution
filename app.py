import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN DE LA PÁGINA ---
# Esto debe ser lo primero que ejecutes en Streamlit
st.set_page_config(
    page_title="Evolución de Habilidades de Datos",
    page_icon="📊",
    layout="wide"
)

# --- FUNCIÓN PARA CARGAR DATOS (con caché) ---
# st.cache_data "recuerda" el resultado. Si los datos no cambian,
# no los vuelve a cargar, haciendo la app más rápida.
@st.cache_data
def load_data():
    df = pd.read_csv('df_metrics.csv', sep=';')
    return df

df = load_data()

# --- TÍTULO Y GANCHO (HOOK) ---
st.title("📊 Evolución de Habilidades en Data Analytics (2012-2022)")

st.markdown("""
Esta aplicación analiza cómo ha cambiado la demanda de habilidades clave en el análisis de datos durante la última década. 
Como especialista en **People Analytics**, mi objetivo es usar datos para responder preguntas críticas de negocio:
* ¿Están nuestras descripciones de puesto **desactualizadas**?
* ¿En qué habilidades deberíamos **invertir** para capacitar a nuestro equipo?
* ¿Dónde está la verdadera **brecha de talento** en el mercado?
""")

st.markdown("---")

# --- EL GRÁFICO INTERACTIVO (Tu análisis principal) ---
st.header("Análisis de Tendencias por Habilidad")
st.write("Usa el gráfico interactivo para explorar la evolución de cada habilidad. Haz doble clic en una habilidad de la leyenda para aislarla.")


umbral_crec_6m = 0
umbral_sharpe = df['ratio_sharpe'].median()


fig = px.scatter(
    df,
    x='crec_ultimos_6m',
    y='ratio_sharpe',
    size='count', # El tamaño de la burbuja
    color='clasificacion', # El color se define por el cuadrante
    hover_name='skills', # Mostrar el nombre del skill al pasar el ratón
    size_max=50, 
    title='Análisis de Evolución de Skills: Crecimiento vs. Estabilidad (Ratio Sharpe)'
)

fig.add_vline(x=umbral_crec_6m, line_width=1, line_dash="dash", line_color="gray")
fig.add_hline(y=umbral_sharpe, line_width=1, line_dash="dash", line_color="gray")

# Etiquetas claras para los ejes
fig.update_layout(
    xaxis_title="Crecimiento Últimos 6m (%)",
    yaxis_title="Ratio de Sharpe (Estabilidad / Bajo Riesgo)"
)

st.plotly_chart(fig, use_container_width=True, key="grafico_cuadrantes_habilidades")
# Muestra el gráfico en Streamlit


# --- CONCLUSIONES (El Insight de People Analytics) ---
st.markdown("---")
st.header("Conclusiones Clave para la Estrategia de Talento")

# Usamos columnas para un layout más limpio
col1, col2 = st.columns(2)

with col1:
    st.subheader("💡 Para Adquisición de Talento (TA)")
    st.write("""
    * **Python es el nuevo Excel:** La demanda de Python ha superado a la de Excel, convirtiéndose en una habilidad fundamental, no solo 'deseable'.
    * **Enfoque en el Stack Moderno:** Las descripciones de puesto deben priorizar el stack 'SQL + Python + Tableau/Power BI'.
    """)

with col2:
    st.subheader("📈 Para Aprendizaje y Desarrollo (L&D)")
    st.write("""
    * **Priorizar el Upskilling:** Los datos muestran una clara dirección para los programas de capacitación internos.
    * **Cerrar la Brecha:** Invertir en Python y herramientas de visualización modernas generará el mayor ROI para preparar a la fuerza laboral.
    """)