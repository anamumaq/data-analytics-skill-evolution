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

st.info("""
    **Objetivo:** Construir un sistema de decisión que separe las tendencias estables (valor real) de las modas volátiles (Hype) 
    analizando los puestos de Analista de Datos en Google Research (2022-2025).
""")


st.markdown("---")
st.header("🔬 Proceso de Análisis y Metodología")

with st.expander("👉 1. El Problema del 'Crecimiento Engañoso' y Volatilidad (Hype)"):
    st.subheader("La Necesidad de Medir la Calidad del Crecimiento")
    st.markdown("""
    El problema de medir la demanda de habilidades es que solo medir el "crecimiento" puede ser engañoso.
    * Una habilidad puede crecer +200 porciento un mes y caer -150 porciento el siguiente. Esto es volatilidad (o Hype para el internet).
    * Otra habilidad puede crecer +10 porciento de forma constante, mes tras mes. Esto es tendencia (Valor Real).
    Basar una decisión de inversión en la primera opción es arriesgado. 
    Es necesario una métrica que mida no solo el crecimiento, sino la calidad y estabilidad de ese crecimiento.
    """)

with st.expander("📊 2. El Framework de Métricas: El 'Filtro de Hype'"):
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

with st.expander("🎯 3. La Matriz de Decisión Estratégica"):
    st.markdown("""
    Al combinar estas métricas, pude crear una matriz 2x2 que funciona como una herramienta para tomar decisiones. 
    En lugar de usar el "crecimiento simple", usé el ratio_sharpe (Calidad de Tendencia) como mi Eje X.
    Esto nos da cuatro perfiles claros para la toma de decisiones:
    """)

st.header("📊 Matriz de Skills")

st.info("""
Importante: Este análisis clasifica las tecnologías basándose en su comportamiento estadístico (Ratio de Sharpe) entre 2022 y 2025.
* "Riesgo/Volatilidad" no significa que la herramienta sea mala; significa que su demanda fluctúa fuertemente (picos de contratación seguidos de pausas).
* "Estabilidad" indica una demanda constante y resistente a las crisis, típica de nichos muy especializados o tecnologías corporativas críticas.
""")
        
tab1, tab2, tab3, tab4 = st.tabs(["Cuadrante 1", "Cuadrante 2", "Cuadrante 3", "Cuadrante 4"])

with tab1:
    st.subheader("Inversión de Crecimiento Sólido")
    st.markdown("""
    * Tecnologías: C++, Go, Java, Pandas, NumPy, Git, SAP, VBA.
    * Análisis: Este cuadrante agrupa dos perfiles opuestos que comparten una característica única: son inmunes a la volatilidad general del mercado.
        * **El perfil "Tech-Heavy"**: Herramientas como **C++, Go y Git** muestran que el mercado está buscando un nuevo tipo de "Analista Técnico" capaz de integrar soluciones en producción, alejándose del analista de negocio tradicional.
        * **El fenómeno "Legacy"**: Sorprendentemente, **VBA y SAP** aparecen aquí. Su estabilidad se debe a que son sistemas críticos en banca y grandes corporaciones; aunque no son "moda", su demanda es inelástica (siempre se necesitan) y hay poca oferta de expertos, lo que garantiza un crecimiento constante.
    """)

with tab2:
    st.subheader("Valor de Portafolio Estable")
    st.markdown("""
    * Tecnologías: Airflow, PL/SQL, Matplotlib, Qlik, Cognos.
    * Análisis: Aquí encontramos las herramientas de "Mantenimiento y Operación".
        * Herramientas como **Airflow o PL/SQL** ya han alcanzado un punto de madurez donde se consideran commodities. No experimentan un "hype" explosivo, pero son requisitos fundamentales en equipos de datos consolidados.
        * Plataformas de BI tradicionales **Qlik, Cognos** se mantienen aquí porque, aunque pierden terreno frente a competidores más nuevos, tienen una base instalada masiva que asegura trabajo constante.
    """)

with tab3:
    st.subheader("Activos de Alto Beta / Volatilidad Extrema")
    st.markdown("""
    * Tecnologías: Python, SQL, Excel, Power BI, Azure, Snowflake, Tableau.
    * Análisis (La aparente contradicción): ¿Por qué las herramientas más populares son "volátiles"?
        * **El Efecto Volumen**: Al ser los estándares del mercado (presentes en el 80-90 porc de ofertas), Python y SQL replican exactamente los ciclos económicos. Cuando hubo congelamiento de contrataciones (2023-2024), su demanda cayó abruptamente; cuando el mercado se reactiva, se disparan.
        * **Interpretación**: Su clasificación de "riesgo" refleja la saturación y la competencia en estos skills, no su falta de utilidad. Son apuestas obligatorias, pero sujetas a los vaivenes de la economía global.
    """)


with tab4:
    st.subheader("Activos en Liquidación")
    st.markdown("""
    * Tecnologías: Spark, Scala, TensorFlow, AWS, GCP, BigQuery.
    * Análisis: Este cuadrante cuenta la historia de la madurez del mercado de datos.
        * **Separación de Roles**: Hace unos años, se pedía a los Analistas que supieran Spark o TensorFlow. Hoy, las empresas han refinado sus descripciones: esas tareas se han movido oficialmente a los roles de **Data Engineer y Machine Learning Engineer**.
        * **La Lectura Correcta**: No es que estas tecnologías estén muriendo (al contrario, son gigantes), es que **su demanda específica dentro del rol de "Data Analyst" está desapareciendo** en favor de perfiles más especializados.
    """)


#--------------------------------------------------------------------
#st.markdown("---")


#st.header("Análisis de Tendencias por Habilidad")
#st.write("Usa el gráfico interactivo para explorar la evolución de cada habilidad. Haz doble clic en una habilidad de la leyenda para aislarla.")

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
    title='Análisis de Evolución de Skills: Crecimiento vs. Estabilidad (Ratio Sharpe)',
    category_orders={
        'clasificacion': [
            '1. Inversión de Crecimiento Sólido',
            '2. Valor de Portafolio Estable', 
            '3. Activos de Alto Beta / Volatilidad Extrema',
            '4. Activos en Liquidación'
        ]
    }
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



