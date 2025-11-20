import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Más Allá del Hype: Framework Estratégico para Data Analyst",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv('df_metrics.csv', sep=';')
    return df

df = load_data()


st.title("📊 Más Allá del Hype: Framework Estratégico para Data Analyst")

st.markdown("""
En un mercado tecnológico ruidoso, **donde cada día nace una nueva herramienta**
¿Dónde invertimos nuestro tiempo y dinero? 
            
Para responder esto analice los puestos de analista de datos en googe research desde el 2022 hasta el 2025.
Con el objetivo de construir un sistema de decisión que separara las tendencias estables de las modas volátiles. 
Este proyecto no es solo un dashboard de frecuencias, es un GPS estratégico para profesionales, educadores y empresas interesadas.
""")

st.markdown("---")
st.header("Proceso de analisis")

st.subheader("1. El Problema del 'Crecimiento Engañoso  ")
st.markdown("""
El problema de medir la demanda de habilidades es que solo medir el "crecimiento" puede ser engañoso.
* Una habilidad puede crecer +200 porciento un mes y caer -150 porciento el siguiente. Esto es volatilidad (o Hype para el internet).
* Otra habilidad puede crecer +10 porciento de forma constante, mes tras mes. Esto es tendencia (Valor Real).
Basar una decisión de inversión en la primera opción es arriesgado. 
Es necesario una métrica que mida no solo el crecimiento, sino la calidad y estabilidad de ese crecimiento.
""")

st.subheader("2. Mi Framework de Métricas")
st.markdown("""
Para resolver esto, diseñé un framework de métricas que va de lo simple a lo estratégico. 
* Métrica Nivel 1: Demanda Actual. Mide el tamaño y la penetración actual de una habilidad. 
* Métrica Nivel 2: Tasa de crecimiento simple (Año vs. Año y últimos 6 meses). Mide la velocidad. Nos dice qué tan rápido se está moviendo una habilidad
* Métrica Nivel 3: El Ratio de "Calidad de Tendencia" (ratio_sharpe) Tomé prestado el Ratio Sharpe, un concepto financiero. 
La fórmula conceptual es: """)

st.latex(r'''
                \text{Ratio Sharpe} = \frac{\text{Crecimiento Promedio (Retorno)}}{\text{Volatilidad de ese Crecimiento (Riesgo)}}
            ''')

st.markdown("""
        Esta métrica es nuestro "filtro de hype".
        *Un Ratio Sharpe bajo* significa que el crecimiento de la habilidad es errático, volátil e impredecible (alto riesgo). Podría ser una moda pasajera.
        *Un Ratio Sharpe alto* significa que el crecimiento es estable, consistente y predecible (bajo riesgo). Esta es una tendencia estructural del mercado.
""")

st.subheader("3. La Matriz de Decisión Estratégica")
st.markdown("""
Al combinar estas métricas, pude crear una matriz 2x2 que funciona como una herramienta para tomar decisiones. 
En lugar de usar el "crecimiento simple", usé el ratio_sharpe (Calidad de Tendencia) como mi Eje X.
Esto nos da cuatro perfiles claros para la toma de decisiones:
""")


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Cuadrante 1: Fundamentales")
    st.write(""" 
    * Alta Demanda y Baja Calidad de Tendencia
    * Qué son: Habilidades maduras, el estándar de la industria (ej. SQL, Excel).
    * La Solución: Son el 'costo de entrada'. No tenerlas te descalifica. Su crecimiento es bajo o estable porque ya están en todas partes
    """)

with col2:
    st.subheader("Cuadrante 2: Estratégicas")
    st.write("""
    *Alta Demanda y Alta Calidad de Tendencia)             
    * Qué son: El "Stack Ganador" (ej. Python, Power BI, Tableau).
    *La Solución: Aquí es donde se debe enfocar la inversión. Tienen alta demanda y un crecimiento estable y probado. Este es el punto dulce del mercado: alta recompensa, bajo riesgo relativo.
    """)

with col3:
    st.subheader("Cuadrante 3: Emergentes")
    st.write("""
    * Baja Demanda y Alta Calidad de Tendencia
    * Qué son: Habilidades de nicho o nuevas con crecimiento muy estable (ej. Snowflake, Databricks).
    * La Solución: Son las "apuestas de futuro". Para un profesional, dominarlas es un diferenciador clave. Para una empresa, es donde debe pilotar su innovación.
    """)


with col4:
    st.subheader("Cuadrante 4: Heredadas ")
    st.write("""
    * Baja Demanda y Baja Calidad de Tendencia
    * Qué son: Habilidades en declive, volátiles o siendo reemplazadas (ej. herramientas propietarias antiguas).
    * La Solución: Representan un riesgo de obsolescencia. Las empresas deben planificar el upskilling y los profesionales deben migrar activamente fuera de aquí.
    """)


#--------------------------------------------------------------------
st.markdown("---")


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

# Etiquetas  para los ejes
fig.update_layout(
    xaxis_title="Crecimiento Últimos 6m (%)",
    yaxis_title="Ratio de Sharpe (Estabilidad / Bajo Riesgo)"
)

st.plotly_chart(fig, use_container_width=True, key="grafico_cuadrantes_habilidades")



# Muestra el gráfico en Streamlit
#--------------------------------------------------------------------

