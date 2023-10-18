import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
st.set_page_config(page_title="Dashboard",page_icon="🌍",layout="wide",)
#st.set_page_config(page_title="Encuesta Oficial delivery ") 

st.header('Resultados Encuestas Nacionales  delivery Bolivia 2023') 
st.subheader('delivery Bolivia 2023') 
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
@st.cache_data
def cargar_datos():
    df = pd.read_spss("BaseFinal.sav")
    df['WPESO']=df['WPESO'].round(0).astype(int)
    df = df.set_index(['nt', 'dia', 'mes', 'ciudad', 'sexo', 'edad', 'edadan', 'EDADX', 'EDADG', 'p3', 'P3G', 'p4', 'P4G', 'p5', 'p6', 'P6X', 'p7', 'P7X', 'P7ME15', 'P7ME15X', 'p8', 'p9', 'p10', 'P10X', 'P10Y', 'p11', 'P11X', 'P11Y', 'P11Z', 'p12', 'p12a', 'p13a', 'p13b', 'P13', 'P13X', 'P13Y', 'p14', 'p10p15', 'p15', 'P15X', 'P15Y', 'p16', 'P16X', 'P16Y', 'P16Z', 'p17', 'p17a', 'p18a', 'p18b', 'P18', 'P18X', 'P18Y', 'p19a', 'p19b', 'P19', 'P19X', 'P19Y', 'p20a', 'p20b', 'p20c', 'p21', 'p15p22', 'p22', 'P22X', 'P22Y', 'p23', 'P23X', 'P23Y', 'P23Z', 'p24', 'p24a', 'p25', 'P25X', 'P25Y', 'p26', 'p27', 'P27X', 'P27Y', 'p28', 'p29a', 'p29b', 'p29c', 'p29d', 'p29e', 'p29f', 'P29AX', 'P29BX', 'P29CX', 'P29DX', 'P29EX', 'P29FX', 'P29SUM', 'P29SUMX', 'p30', 'P30WP', 'p30a', 'P30AX', 'P30AY', 'p31a', 'p31b', 'p31c', 'p31d', 'p31e', 'p31f', 'p31g', 'p31h', 'p31i', 'p31j', 'p31k', 'p31l', 'p31m', 'p31n', 'P31AY', 'P31BY', 'P31CY', 'P31DY', 'P31EY', 'P31FY', 'P31GY', 'P31HY', 'P31IY', 'P31JY', 'P31KY', 'p32', 'p32a', 'p33', 'p34', 'p35', 'p36a', 'p36b', 'p36c', 'p37', 'p37bs', 'p37t', 'p38', 'p39', 'p40a1', 'p40a2', 'p40b1', 'p40b2', 'p40c1', 'p40c2', 'p40d1', 'p40d2', 'p40e1', 'p40e2', 'p40f1', 'p40f2', 'P40A1Y', 'P40B1Y', 'P40C1Y', 'P40D2Y', 'P40E2Y', 'P40F2Y', 'P40A2Y', 'P40B2Y', 'P40C2Y', 'p41', 'p42', 'P42X', 'P42Y', 'p43a', 'p43b', 'p43c', 'p43d', 'p43e', 'P43AY', 'P43BY', 'P43CY', 'P43DY', 'P43EY', 'p43f', 'p43g', 'p43h', 'p44', 'p45a', 'p45b', 'P45AY', 'P45BY', 'p45c', 'p45d', 'p45e', 'p46', 'p46p52', 'p47', 'P47X', 'p48', 'p49', 'p50', 'P50X', 'P50Y', 'p51', 'p52', 'p53a', 'p53b', 'p53c', 'p54', 'p55a', 'p55b', 'p55c', 'p56', 'p57a1', 'P57A1X', 'P57A1Y', 'p58a1', 'P58A1X', 'P58A1Y', 'p58b1', 'P58B1X', 'P58B1Y', 'p57a2', 'P57A2X', 'P57A2Y', 'P57A3', 'P57A3X', 'P57A3Y', 'p58a2', 'P58A2X', 'P58A2Y', 'p58b2', 'P58B2X', 'P58B2Y', 'p59', 'p60a1', 'P60A1X', 'P60A1Y', 'p60a2', 'P60A2X', 'P60A2Y', 'P60A3', 'P60A3X', 'P60A3Y', 'p61', 'p62', 'p63', 'p64', 'p64a', 'p65', 'P65X', 'p66a', 'P66AX', 'P66AY', 'p66b', 'P66BX', 'P66BY', 'p67a', 'p67b', 'P67', 'P67X', 'P67Y', 'p68', 'P68X', 'P68Y', 'P68MES', 'P68MESX', 'P68MESY', 'p69a', 'P69AX', 'P69AY', 'p69b', 'P69BX', 'P69BY', 'p70', 'p71', 'p71a', 'p71b', 'p72m1lu1', 'p72m1lu2', 'p72m1lu3', 'p72m1lu4', 'p72m1lu5', 'p72m1ma1', 'p72m1ma2', 'p72m1ma3', 'p72m1ma4', 'p72m1ma5', 'p72m1mi1', 'p72m1mi2', 'p72m1mi3', 'p72m1mi4', 'p72m1mi5', 'p72m1ju1', 'p72m1ju2', 'p72m1ju3', 'p72m1ju4', 'p72m1ju5', 'p72m1vi1', 'p72m1vi2', 'p72m1vi3', 'p72m1vi4', 'p72m1vi5', 'p72m1sa1', 'p72m1sa2', 'p72m1sa3', 'p72m1sa4', 'p72m1sa5', 'p72m1do1', 'p72m1do2', 'p72m1do3', 'p72m1do4', 'p72m1do5', 'P72M1LUH', 'P72M1MAH', 'P72M1MIH', 'P72M1JUH', 'P72M1VIH', 'P72M1SAH', 'P72M1DOH', 'p72m2lu1', 'p72m2lu2', 'p72m2lu3', 'p72m2lu4', 'p72m2lu5', 'p72m2ma1', 'p72m2ma2', 'p72m2ma3', 'p72m2ma4', 'p72m2ma5', 'p72m2mi1', 'p72m2mi2', 'p72m2mi3', 'p72m2mi4', 'p72m2mi5', 'p72m2ju1', 'p72m2ju2', 'p72m2ju3', 'p72m2ju4', 'p72m2ju5', 'p72m2vi1', 'p72m2vi2', 'p72m2vi3', 'p72m2vi4', 'p72m2vi5', 'p72m2sa1', 'p72m2sa2', 'p72m2sa3', 'p72m2sa4', 'p72m2sa5', 'p72m2do1', 'p72m2do2', 'p72m2do3', 'p72m2do4', 'p72m2do5', 'P72M2LUH', 'P72M2MAH', 'P72M2MIH', 'P72M2JUH', 'P72M2VIH', 'P72M2SAH', 'P72M2DOH', 'p72m3lu1', 'p72m3lu2', 'p72m3lu3', 'p72m3lu4', 'p72m3lu5', 'p72m3ma1', 'p72m3ma2', 'p72m3ma3', 'p72m3ma4', 'p72m3ma5', 'p72m3mi1', 'p72m3mi2', 'p72m3mi3', 'p72m3mi4', 'p72m3mi5', 'p72m3ju1', 'p72m3ju2', 'p72m3ju3', 'p72m3ju4', 'p72m3ju5', 'p72m3vi1', 'p72m3vi2', 'p72m3vi3', 'p72m3vi4', 'p72m3vi5', 'p72m3sa1', 'p72m3sa2', 'p72m3sa3', 'p72m3sa4', 'p72m3sa5', 'p72m3do1', 'p72m3do2', 'p72m3do3', 'p72m3do4', 'p72m3do5', 'P72M3LUH', 'P72M3MAH', 'P72M3MIH', 'P72M3JUH', 'P72M3VIH', 'P72M3SAH', 'P72M3DOH', 'P72LU', 'P72LUX', 'P72LUY', 'P72MA', 'P72MAX', 'P72MAY', 'P72MI', 'P72MIX', 'P72MIY', 'P72JU', 'P72JUX', 'P72JUY', 'P72VI', 'P72VIX', 'P72VIY', 'P72SA', 'P72SAX', 'P72SAY', 'P72DO', 'P72DOX', 'P72DOY', 'P72HRS', 'P72HRSX', 'P72HRSY', 'p76a', 'P76AX', 'P76AY', 'P76AG', 'p76b', 'P76BX', 'P76BY', 'P76BG', 'p76c', 'P76CX', 'P76CY', 'P76CG', 'p77', 'p78a', 'p78b', 'p78c', 'p78d', 'p79', 'P79X', 'P79Y', 'p79km', 'P79KMX', 'p80', 'p80a', 'P80AX', 'P80AY', 'p80b', 'P80BX', 'P80BY', 'p82a', 'P82AY', 'p82b', 'P82BY', 'p82c', 'P82CY', 'p82d', 'P82DY', 'p82e', 'P82EY', 'p82f', 'P82FY', 'p82g', 'P82GY', 'p82h', 'p82i', 'p82j', 'p85a', 'P85AX', 'P85AY', 'P85AG', 'p85b', 'P85BX', 'P85BY', 'P85BG', 'p86a', 'P86AY', 'p86b', 'P86BY', 'p86c', 'P86CY', 'p86d', 'P86DY', 'p86e', 'p86f', 'p86g', 'p87', 'p88', 'p89a', 'p89b', 'p89c', 'p90', 'p90a', 'P90AY', 'p90b', 'P90BY', 'p90c', 'P90CY', 'p90d', 'P90DY', 'p91', 'p91a', 'P91AY', 'p91b', 'P91BY', 'p91c', 'P91CY', 'p91d', 'P91DY', 'p92a', 'P92AY', 'p92b', 'P92BY', 'p92c', 'P92CY', 'p92d', 'P92DY', 'p93', 'p94a', 'P94AY', 'p94b', 'P94BY', 'p94d', 'P94DY', 'p94c', 'P94CY', 'p95', 'p96', 'p97a', 'p97b', 'p97c', 'p98a1', 'p98a2', 'P98A2X', 'p98a3', 'p98b1', 'p98b2', 'P98B2X', 'P98B2DIA', 'P98B2SEM', 'P98B2FIN', 'P98B2MES', 'P98B2DIAG', 'P98B2SEMG', 'p98b3', 'p98c', 'p99a', 'P99AY', 'p99b', 'P99BY', 'p99c', 'P99CY', 'p99d', 'p100', 'p101a', 'P101AY', 'P101AG', 'p101b', 'P101BY', 'P101BG', 'p101c', 'P101CY', 'P101CG', 'p102a', 'P102AY', 'P102AG', 'p102b', 'P102BG', 'P102BY', 'p102c', 'P102CY', 'P102CG', 'p103', 'p104', 'p105', 'p106a', 'p106b', 'p106c', 'p107a', 'p107b', 'p107c', 'p107d', 'p107e', 'p108', 'p108a', 'P108AG', 'p108b', 'P108BG', 'p108c', 'P108CG', 'p109', 'p110', 'p110a', 'P110AG', 'p110b', 'P110BG', 'p110c', 'P110CG', 'p111a', 'P111AG', 'p111b', 'P111BG', 'p111c', 'P111CG', 'p112a', 'p112b', 'p112c', 'p112d', 'p112e', 'p112f', 'p112g', 'da1a', 'da1b', 'da1c', 'xnt', 'obs1', 'obs2', 'obs3', 'obs4', 'obs5', 'obs6', 'obs7', 'obs8', 'obs9', 'obs10', 'EMPR', 'LU0', 'LU1', 'LU2', 'LU3', 'LU4', 'LU5', 'LU6', 'LU7', 'LU8', 'LU9', 'LU10', 'LU11', 'LU12', 'LU13', 'LU14', 'LU15', 'LU16', 'LU17', 'LU18', 'LU19', 'LU20', 'LU21', 'LU22', 'LU23', 'P72M1LUHx', 'P72M2LUHx', 'P72M3LUHx', 'MA0', 'MA1', 'MA2', 'MA3', 'MA4', 'MA5', 'MA6', 'MA7', 'MA8', 'MA9', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'P72M1MAHx', 'P72M2MAHx', 'P72M3MAHx', 'MI0', 'MI1', 'MI2', 'MI3', 'MI4', 'MI5', 'MI6', 'MI7', 'MI8', 'MI9', 'MI10', 'MI11', 'MI12', 'MI13', 'MI14', 'MI15', 'MI16', 'MI17', 'MI18', 'MI19', 'MI20', 'MI21', 'MI22', 'MI23', 'P72M1MIHx', 'P72M2MIHx', 'P72M3MIHx', 'JU0', 'JU1', 'JU2', 'JU3', 'JU4', 'JU5', 'JU6', 'JU7', 'JU8', 'JU9', 'JU10', 'JU11', 'JU12', 'JU13', 'JU14', 'JU15', 'JU16', 'JU17', 'JU18', 'JU19', 'JU20', 'JU21', 'JU22', 'JU23', 'P72M1JUHx', 'P72M2JUHx', 'P72M3JUHx', 'VI0', 'VI1', 'VI2', 'VI3', 'VI4', 'VI5', 'VI6', 'VI7', 'VI8', 'VI9', 'VI10', 'VI11', 'VI12', 'VI13', 'VI14', 'VI15', 'VI16', 'VI17', 'VI18', 'VI19', 'VI20', 'VI21', 'VI22', 'VI23', 'P72M1VIHx', 'P72M2VIHx', 'P72M3VIHx', 'SA0', 'SA1', 'SA2', 'SA3', 'SA4', 'SA5', 'SA6', 'SA7', 'SA8', 'SA9', 'SA10', 'SA11', 'SA12', 'SA13', 'SA14', 'SA15', 'SA16', 'SA17', 'SA18', 'SA19', 'SA20', 'SA21', 'SA22', 'SA23', 'P72M1SAHx', 'P72M2SAHx', 'P72M3SAHx', 'DO0', 'DO1', 'DO2', 'DO3', 'DO4', 'DO5', 'DO6', 'DO7', 'DO8', 'DO9', 'DO10', 'DO11', 'DO12', 'DO13', 'DO14', 'DO15', 'DO16', 'DO17', 'DO18', 'DO19', 'DO20', 'DO21', 'DO22', 'DO23', 'P72M1DOHx', 'P72M2DOHx', 'P72M3DOHx', 'P72LU2', 'P72MA2', 'P72MI2', 'P72JU2', 'P72VI2', 'P72SA2', 'P72DO2', 'P72NDIAS', 'P72NDIASX', 'P72INILU', 'P72INIMA', 'P72INIMI', 'P72INIJU', 'P72INIVI', 'P72INISA', 'P72INIDO', 'P72PEDLU', 'P72PEDMA', 'P72PEDMI', 'P72PEDJU', 'P72PEDVI', 'P72PEDSA', 'P72PEDDO', 'P72PED', 'P72PEDLUX', 'P72PEDLUY', 'P72PEDMAX', 'P72PEDMAY', 'P72PEDMIX', 'P72PEDMIY', 'P72PEDJUX', 'P72PEDJUY', 'P72PEDVIX', 'P72PEDVIY', 'P72PEDSAX', 'P72PEDSAY', 'P72PEDDOX', 'P72PEDDOY', 'P72PEDX', 'P72PEDY', 'INGPED'])['WPESO']\
        .repeat(df['WPESO'])\
        .reset_index()
    return df
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("http://cedla.org/wp-content/uploads/2023/10/fondo.png");

background-position: top left;
background-repeat: repeat;

}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
df=cargar_datos()

Genero = df['sexo'].unique().tolist()
df['edad'] = df['edad'].astype(int)
edad=df['edad'].unique().tolist()
Ciudad = df['ciudad'].unique().tolist()

with st.sidebar:
    st.image("cedla.png", use_column_width=True,width=100)
    st.header('Resultados Encuestas Nacionales  delivery Bolivia 2023') 
    st.markdown('Los trabajos de reparto surgen de los nuevos tipos de trabajos de la economía “Gig”.  Los repartidores desempeñan un papel fundamental para garantizar la circulación fluida de los bienes de las empresas a los consumidores. En Bolivia, este fenómeno también está presente. ',)
    edad_selector = st.slider("Edad persona encuestada:",
                          min_value = min(edad), #el valor minimo va a ser el valor mas pequeño que encuentre dentro de la columna EDAD PERSONA ENCUESTADA
                          max_value = max(edad),#el valor maximo va a ser el valor mas grande que encuentre dentro de la columna EDAD PERSONA ENCUESTADA
                          value = (min(edad),max(edad)))
    Generos=['Hombre','Mujer']
    calificacion_genero =[]
    for genero in Generos:
        if st.checkbox(genero,value=True):
         calificacion_genero.append(genero)   
    
    ciudades = ['La Paz', 'El Alto', 'Santa Cruz','Cochabamba']
    st.write("Ciudades:")
# Crear casillas de verificación para cada ciudad
    seleccionadas = []
    for ciudad in ciudades:
        if st.checkbox(ciudad,value=True):
         seleccionadas.append(ciudad)

# Imprimir las ciudades seleccionadas
    
def P(p20a):
    if p20a == 'Mejores posibilidades de ingreso':
        return 'Mejores posibilidades de ingreso' 
    if p20a == 'Mayor libertad de horarios':
        return 'Mayor libertad de horario' 
    if p20a == 'Era la única opción de trabajo disponible':
        return 'Era la única opción de trabajo'
    else:
        return 'Otros'
def f(p67b):
    if p67b == 'Semana':
        return 4
    if p67b == 'Quincena':
        return 2
    if p67b == 'Mes':
        return 1
    if p67b == 'Trimestre':
        return 0.33 
    else:
        return 0.17
def d(dependencia):
    if dependencia == 0:
        return 'Nadie'
    if dependencia == 1 or dependencia == 2:
        return 'Hasta dos' 
    else:
        return 'Mas de dos'
def x(p60a1):
    if p60a1 == 'Ns/Nr':
        return 2000
    else:
        return p60a1
def years_of_study(p4):
    if p4 == 'Ninguno' or p4 == 'Primaria completa' or p4 == 'Secundaria incompleta' or p4 == 'Secundaria completa' :
        return 'Secundario'
    if p4=='Superior incompleta (técnico/ universitario)':
        return 'Superior incompleta'
    else:
        return 'Superior'
def asalariado(anterior):
    if anterior ==  'Empleado' or anterior == 'Obrero' or anterior == 'Profesional independiente/ Consultor':
        return 'asalariado'
    else:
        return 'no asalariado'
def jefe(p8):
    if p8 == 'Jefe o jefa del hogar':
        return 'jefe'
    else:
        return 'no jefe'
def m(pluriactividad):
    if pluriactividad == 'Solo trabaja como delivery':
        return 'Solo trabaja como delivery'
    else:
        return 'Alterna con otro trabajo y/o estudios'
def z(razones):
    if razones == 'Era un empleo temporal':
        return 'Era un empleo temporal'
    if razones == 'Fue despedido' or razones == 'La empresa, negocio, actividad se cerró' or razones == 'Por falta de capital o de clientes' or razones =='Fue obligado a renunciar':
        return 'Razones de la demanda'
    if razones == 'Razones personales':
        return 'Razones personales'
    if razones == 'Razones económicas/ bajos ingresos':
        return 'Razones económicas/ bajos ingresos'
    else:
        return 'Renuncio'
def t(menores):
    if menores == 0:
        return 'ninguno'
    else:
        return 'menores en el hogar'
def anti(antiguedad):
    if antiguedad <=  12:
        return 1
    if antiguedad <= 24:
        return 2
    if antiguedad <= 33:
        return 3
    else:
        return 4
def a(PrimeroTrabajo):
    if PrimeroTrabajo == 'Primertrabajo':
        return 'Primer trabajo'
    else:
        return'Tenía trabajo'
def o(edad):
    if 18 <= edad <= 24:
        return "joven"
    if 25 <= edad <= 30:
        return "joven adulto"
    else:
        return "adulto"    
def years_of_study2(educacion):
    if educacion == 'Ninguno':
        return 0
    if educacion == 'Primaria completa':
        return 5
    if educacion == 'Secundaria incompleta':
        return 10
    if educacion == 'Secundaria completa':
        return 11
    if educacion == 'Superior incompleta (técnico/ universitario)':
        return 13
    if educacion == 'Superior completa (técnico/ universitario)':
        return 15
    else:
        return 16
column_headers = list(df.columns.values)
df['dependencia'] = df['p65'].astype(int)
df['dependencia'] = df['dependencia'].apply(d)
df1 = df[['edad']]
dfn1 = df['p60a1']
df['p67b'] = df['p67b'].fillna('Mes')
df['periodo'] = df['p67b'].apply(f)
df['periodo'] = df['periodo'].astype(int)
df['p67a'] = df['p67a'].astype(int)
df['mantenimiento'] = df['p67a'] * df['periodo']
df['p66a'] = df['p66a'].astype(int)
df['p66b'] = df['p66b'].astype(int)
df['gastos'] = df['mantenimiento'] + df['p66a'] + df['p66b']
df['ingresom'] = df['p60a1'].apply(x)
df['ingresor'] = df['ingresom'] - df['gastos']
df['categoria'] = df['ingresor'].apply(lambda x: 'Mínimo' if x < 2250 else 'Medio' if x < 4500 else 'Alto')

df3 = df[['categoria','p4']]
df3['educacion'] = df3['p4'].apply(years_of_study2)
df3['Horarios']=df['P72HRS']
df3.drop(columns=['p4'], inplace=True)

df['years of study'] = df['p4'].apply(years_of_study)
df.rename(columns={'years of study':'educacion'}, inplace=True)
df['jefe'] = df['p8'].apply(jefe)
df['jefe'].value_counts()
df['anterior'] = df['p12']
df['anterior'] = df['anterior'].apply(asalariado)
df['antiguedad'] = df['p27']
df['antiguedad'] = df['antiguedad'].apply(anti)
df['categoria2'] = df['edad'].apply(o)

df['pluriactividad'] = df['p21']
df['pluriactividad'] = df['pluriactividad'].apply(m)
df['razones'] = df['p14']
#Crear un slider de edad
df['razones'] = df['razones'].apply(z)
df['p7'] = df['p7'].fillna(0)
df['menores'] = df['p7'].astype(int)
df['menores'] = df['menores'].apply(t)
df2 = df[['edad', 'razones','pluriactividad', 'antiguedad', 'ingresor', 'categoria', 'educacion', 'jefe','anterior','menores','dependencia']]
df2['edad'] = df2['edad'].astype(int)
df['p12']=df['p12'].cat.add_categories('Primertrabajo').fillna('Primertrabajo')
df['PrimeroTrabajo']=df['p12']
df['PrimeroTrabajo'] = df['PrimeroTrabajo'].apply(a)
df['menores'] = df['menores'].apply(t)
df2 = df[['PrimeroTrabajo','edad', 'razones','pluriactividad', 'antiguedad', 'ingresor', 'categoria', 'educacion', 'jefe','anterior','menores','dependencia','WPESO']]
df2['edad'] = df2['edad'].astype(int)

edad=df2['edad'].unique().tolist()
Primer_Trabajo = df2['PrimeroTrabajo'].unique().tolist()

fig = go.Figure(go.Sunburst(
    labels=["\n", "Más de 30", "De 25 a 29", "De 18 a 24","Hombre","Mujer","Hombre ","Mujer ","Hombre  ","Mujer  "],
    parents=["", "\n", "\n", "\n", "De 18 a 24", "De 18 a 24","De 25 a 29","De 25 a 29",
             "Más de 30","Más de 30"], maxdepth=2,
    sort=False, 
    values=[1000,994,1816,1405,1376,29,1699,117,939,55],
))
fig.update_layout(title='Edad de los repartidores ', margin=dict(l=50, r=50, b=50, t=50))

left,center,right=st.columns(3)
center.plotly_chart(fig,use_container_width=True)

mask = (df2['edad'].between(*edad_selector))&(df['sexo'].isin(calificacion_genero))&(df['ciudad'].isin(seleccionadas))
numero_resultados = df2[mask].shape[0]


df_agrupado = df2[mask].groupby(by=['PrimeroTrabajo']).count()[['edad']] #que me agrupe por CALIFICACION y me cuente por los datos de  EDAD PERSONA ENCUESTADA
df_agrupado =df_agrupado.reset_index()
df_agrupado =df_agrupado.rename(columns={'edad': 'Numero de repartidores'})
df_agrupado =df_agrupado.rename(columns={'PrimeroTrabajo': 'Fuente CEDLA encuesta delivery 2022'})
suma_edades = df_agrupado['Numero de repartidores'].sum( )
df_agrupado['Porcentaje'] = ((df_agrupado['Numero de repartidores'] / suma_edades) * 100).round(0).astype(int)
colores_personalizados = ['#ff4e50'] 
if len(df_agrupado) == 2:
    colores_personalizados = ['#ff4e50','#fc913a']  # Longitud 1
if len(df_agrupado) == 1:
    colores_personalizados = ['#ff4e50']  # Longitud 2
df_agrupado['color'] = colores_personalizados
bar_chart = px.bar(df_agrupado, 
                   x='Fuente CEDLA encuesta delivery 2022',
                   y='Porcentaje',
                   text='Porcentaje',
                   color='color',
                   color_discrete_sequence=colores_personalizados,
                   template = 'plotly_white')
bar_chart.update_traces(textfont=dict(size=15))
bar_chart.update_layout(showlegend=False,title='Porcentaje de repartidores que tenían un trabajo anterior.')








mask4 = (df2['edad'].between(*edad_selector))&(df['ciudad'].isin(seleccionadas))&(df['sexo'].isin(calificacion_genero))
numero_resultados4 = df[mask4].shape[0]

df_agrupado4 = df[mask4].groupby(by=['pluriactividad']).count()[['edad']] #que me agrupe por CALIFICACION y me cuente por los datos de  EDAD PERSONA ENCUESTADA
df_agrupado4 =df_agrupado4.reset_index()
suma_edades4 = df_agrupado4['edad'].sum( )

df_agrupado4['Porcentaje'] = ((df_agrupado4['edad'] / suma_edades4) * 100).round(0).astype(int)
if len(df_agrupado4)==4:
    colores_personalizados = ['#ff4e50', '#fc913a', '#f9d423','#ecec53']
if len(df_agrupado4) == 3:
    colores_personalizados = ['#ff4e50', '#fc913a', '#f9d423']
if len(df_agrupado4)==2:
    colores_personalizados = ['#ff4e50', '#fc913a']
if len(df_agrupado4)==1:
    colores_personalizados = ['#ff4e50']
df_agrupado4['color'] = colores_personalizados
df_agrupado4 =df_agrupado4.rename(columns={'pluriactividad': 'Fuente CEDLA encuesta delivery 2022'})
bar_chartP = px.bar(df_agrupado4, 
                   x='Fuente CEDLA encuesta delivery 2022',
                   y='Porcentaje',
                   text='Porcentaje',
                   color='color',
                   color_discrete_sequence=colores_personalizados,
                   template='plotly_white',
                   category_orders={"Fuente CEDLA encuesta delivery 2022":["Mejores posibilidades de ingreso","Mayor libertad de horario","Otros","Era la única opción de trabajo" ]})
bar_chartP.update_traces(textfont=dict(size=15))
bar_chartP.update_layout(showlegend=False,title='Repartidores y pluriactividad')

df['m'] = df['p20a'].apply(P)
st.subheader('Repartidores con trabajo anterior y pluriactividad') 
Razon= df['m'].unique().tolist()

left,right=st.columns(2)
left.plotly_chart(bar_chart,use_container_width=True)
right.plotly_chart(bar_chartP,use_container_width=True)
st.subheader('Ingreso según el nivel de estudio') 
edad2=df2['edad'].unique().tolist()
Nivel_Estudio = df['educacion'].unique().tolist()
Pruactividad = df['pluriactividad'].unique().tolist()
calificacion_Estudio = st.multiselect('Estudio:',
                                       Nivel_Estudio,
                                       default = Nivel_Estudio)

mask2 = (df2['edad'].between(*edad_selector))& (df['educacion'].isin(calificacion_Estudio))&(df['ciudad'].isin(seleccionadas))&(df['sexo'].isin(calificacion_genero))
numero_resultados2 = df[mask2].shape[0]

df_agrupado2 = df2[mask2].groupby(by=['educacion']).count()[['edad']] #que me agrupe por CALIFICACION y me cuente por los datos de  EDAD PERSONA ENCUESTADA
df_agrupado2 =df_agrupado2.reset_index()
suma_edades2 = df_agrupado2['edad'].sum( )
df_agrupado2 =df_agrupado2.rename(columns={'edad': 'Numero de repartidores'})
df_agrupado2 =df_agrupado2.rename(columns={'educacion': 'Fuente CEDLA encuesta delivery 2022'})
df_agrupado2['Porcentaje'] = ((df_agrupado2['Numero de repartidores'] / suma_edades2) * 100).round(0).astype(int)

if len(df_agrupado2) == 3:
    colores_personalizados = ['#ff4e50', '#f9d423','#fc913a']
if len(df_agrupado2)==2:
    colores_personalizados = ['#ff4e50', '#fc913a']
if len(df_agrupado2)==1:
    colores_personalizados = ['#ff4e50']

df_agrupado2['color'] = colores_personalizados

bar_chart2 = px.bar(df_agrupado2, 
                   x='Fuente CEDLA encuesta delivery 2022',
                   y='Porcentaje',           
                   text='Porcentaje',
                   color='color',
                   color_discrete_sequence=colores_personalizados,
                   template = 'plotly_white',
                   category_orders={"Fuente CEDLA encuesta delivery 2022":["Secundario","Superior incompleta","Superior" ]}
                   )
bar_chart2.update_traces(textfont=dict(size=15))
bar_chart2.update_layout(showlegend=False,title="Nivel de estudios de los delivery")

# Ingresos

edad3=df2['edad'].unique().tolist()
Nivel_Ingreso = df2['categoria'].unique().tolist()

calificacion_ingresor = st.multiselect('Ingreso:',
                                       Nivel_Ingreso,
                                       default = Nivel_Ingreso)

mask3 = (df2['edad'].between(*edad_selector))& (df2['categoria'].isin(calificacion_ingresor))&(df['ciudad'].isin(seleccionadas))&(df['sexo'].isin(calificacion_genero))
numero_resultados3 = df[mask3].shape[0]

df_agrupado3 = df2[mask3].groupby(by=['categoria']).count()[['edad']] #que me agrupe por CALIFICACION y me cuente por los datos de  EDAD PERSONA ENCUESTADA
df_agrupado3 =df_agrupado3.reset_index()
df_agrupado3 =df_agrupado3.rename(columns={'edad': 'Numero de repartidores'})
df_agrupado3 =df_agrupado3.rename(columns={'categoria': 'Fuente CEDLA encuesta delivery 2022'})
suma_edades3 = df_agrupado3['Numero de repartidores'].sum( )
df_agrupado3['Porcentaje'] = ((df_agrupado3['Numero de repartidores'] / suma_edades3) * 100).round(0).astype(int)

if len(df_agrupado3) == 3:
    colores_personalizados = ['#f9d423','#fc913a', '#ff4e50']
if len(df_agrupado3)==2:
    colores_personalizados = ['#ff4e50', '#fc913a']
if len(df_agrupado3)==1:
    colores_personalizados = ['#ff4e50']
df_agrupado3['color'] = colores_personalizados
bar_chart3 = px.bar(df_agrupado3, 
                   x='Fuente CEDLA encuesta delivery 2022',
                   category_orders={"Fuente CEDLA encuesta delivery 2022":["Mínimo","Medio","Alto"]},
                   y='Porcentaje',
                   text='Porcentaje',
                   color='color',
                   color_discrete_sequence=colores_personalizados,  # Asigna los colores personalizados aquí
                   template='plotly_white'
                  )
bar_chart3.update_traces(textfont=dict(size=15))
bar_chart3.update_layout(showlegend=False,title='Nivel de ingresos de los deliverys ')
left,right=st.columns(2)
left.plotly_chart(bar_chart2,use_container_width=True)
right.plotly_chart(bar_chart3,use_container_width=True)
st.markdown('<p style="color: white;">Mínimo hace referencia a que el repartidor ganó hasta un salario mínimo. Medio nos dice que el delivery ganó entre uno y dos salarios mínimos. Alto significa que el trabajador de plataforma tuvo ingresos de más de dos salarios mínimos..</p>',unsafe_allow_html=True)

dff = df[['razones']]
dff.dropna()
dff['razones'] = dff['razones'].astype(str)
text = ' '.join(dff['razones'].astype(str))
# Create the WordCloud
st.subheader('Motivación para trabajar como delivery') 

# Muestra la imagen en la aplicación de Streamlit
opciones_seleccionadas = st.multiselect('Motivos:',
                                       Razon,
                                       default = Razon)
mask4 = (df2['edad'].between(*edad_selector))& (df['m'].isin(opciones_seleccionadas))&(df['ciudad'].isin(seleccionadas))&(df['sexo'].isin(calificacion_genero))
numero_resultados4 = df[mask4].shape[0]

df_agrupado4 = df[mask4].groupby(by=['m']).count()[['edad']] #que me agrupe por CALIFICACION y me cuente por los datos de  EDAD PERSONA ENCUESTADA
df_agrupado4 =df_agrupado4.reset_index()
suma_edades4 = df_agrupado4['edad'].sum( )

df_agrupado4['Porcentaje'] = ((df_agrupado4['edad'] / suma_edades4) * 100).round(0).astype(int)
if len(df_agrupado4)==4:
    colores_personalizados = ['#ff4e50', '#fc913a', '#f9d423','#ecec53']
if len(df_agrupado4) == 3:
    colores_personalizados = ['#ff4e50', '#fc913a', '#f9d423']
if len(df_agrupado4)==2:
    colores_personalizados = ['#ff4e50', '#fc913a']
if len(df_agrupado4)==1:
    colores_personalizados = ['#ff4e50']
df_agrupado4['color'] = colores_personalizados
df_agrupado4 =df_agrupado4.rename(columns={'m': 'Fuente CEDLA encuesta delivery 2022'})
bar_chart4 = px.bar(df_agrupado4, 
                   x='Fuente CEDLA encuesta delivery 2022',
                   y='Porcentaje',
                   text='Porcentaje',
                   color='color',
                   color_discrete_sequence=colores_personalizados,
                   template='plotly_white',
                   category_orders={"Fuente CEDLA encuesta delivery 2022":["Mejores posibilidades de ingreso","Mayor libertad de horario","Otros","Era la única opción de trabajo" ]})
bar_chart4.update_traces(textfont=dict(size=15))
bar_chart4.update_layout(showlegend=False)

left,right=st.columns(2)
left.plotly_chart(bar_chart4,use_container_width=True)

st.subheader("Click en el boton para ver la imagen")
left,right,center=st.columns(3)

if left.button("18 a 24", type="primary",use_container_width=True ,key="age_1"):
   imagen=st.image("18 a 24.jpg", use_column_width=True,width=100)
if right.button("25 a 29",type="primary",use_container_width=True,key="age_2"):
   
   imagen=st.image("25 a 29.jpg", use_column_width=True,width=1200)
if center.button("30 a 50", type="primary",use_container_width=True,key="age_3"):
   imagen=st.image("30 a 50.jpg", use_column_width=True,width=50)


educacionm= df3['educacion'].unique().tolist()
grouped_data = df3.groupby('categoria')['Horarios'].mean().reset_index()
# Crear una figura de Plotly con un gráfico de líneas y marcadores para 'Horarios'
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Agregar una traza de tipo 'go.Scatter' para 'Horas' en el eje izquierdo
fig.add_trace(
    go.Scatter(
        x=grouped_data['categoria'],
        y=grouped_data['Horarios'],
        mode='lines+markers',  # Indica que queremos una línea con marcadores
        name='Horas',  # Nombre para la primera línea
        line=dict(color="coral"),  # Color para la línea de 'Horas'
        marker=dict(color="coral", size=10),
        text=grouped_data['Horarios'],  # Etiquetas de texto para los puntos
        textposition='top right',  # Coloca las etiquetas en la parte superior derecha
    ),
    secondary_y=False  # Asigna esta traza al eje y principal (izquierdo)
)

# Agregar una traza de tipo 'go.Scatter' para 'Educación' en el eje derecho
fig.add_trace(
    go.Scatter(
        x=grouped_data['categoria'],
        y=educacionm,
        mode='lines+markers',  # Indica que queremos una línea con marcadores
        name='Educación',  # Nombre para la segunda línea
        line=dict(color="blue"),  # Color para la línea de 'Educación'
        marker=dict(color="blue", size=10),
        text=educacionm,  # Etiquetas de texto para los puntos
        textposition='top left',  # Coloca las etiquetas en la parte superior izquierda
      
    ),
    secondary_y=True  # Asigna esta traza al eje y secundario (derecho)
)

# Personalizar el diseño del gráfico
fig.update_xaxes(categoryorder="array", categoryarray=["Mínimo", "Medio", "Alto"])
fig.update_yaxes(title_text="Horas Trabajadas", secondary_y=False)
fig.update_yaxes(title_text="Educación", secondary_y=True)
fig.update_layout(
    xaxis_title='Ingreso por salario mínimo'  
)

# Mostrar el gráfico con ambas líneas
st.subheader("Educación y cantidad de horas trabajadas por los delivery")
st.plotly_chart(fig)
