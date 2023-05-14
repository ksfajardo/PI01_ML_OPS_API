
import pandas as pd
import numpy as np
import locale


df=pd.read_csv('data/Movies_ETL_EDA.csv')




""" def peliculas_mes(mes):
    fechas=pd.to_datetime(df['release_date'],format='%Y-%m-%d')
    nmes=fechas[fechas.dt.month_name(locale='es_CO')==mes.capitalize()]
    respuesta=nmes.shape[0]
    return {'mes':mes, 'cantidad':respuesta} """


def peliculas_mes(mes):
    # Set the locale to Spanish
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    
    fechas = pd.to_datetime(df['release_date'], format='%Y-%m-%d')
    nmes = fechas[fechas.dt.strftime('%B').str.capitalize() == mes.capitalize()]
    respuesta = nmes.shape[0]
    return {'mes': mes, 'cantidad': respuesta}






""" def peliculas_dia(dia):
    fechas=pd.to_datetime(df['release_date'],format='%Y-%m-%d')
    ndia=fechas[fechas.dt.day_name(locale='es_CO')==dia.capitalize()]
    respuesta=ndia.shape[0]
    return {'dia':dia, 'cantidad':respuesta} """


def peliculas_dia(dia):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    fechas=pd.to_datetime(df['release_date'],format='%Y-%m-%d')
    ndia = fechas[fechas.dt.strftime('%A') == dia.lower()]
    respuesta=ndia.shape[0]
    return {'dia':dia, 'cantidad':respuesta}







def franquicia(franquicia):
    f_low=franquicia.lower()
    fran=df[['collection_name','budget','revenue']].dropna(subset=['collection_name'])
    fran=fran[fran['collection_name'].map(str.lower).apply(lambda x: f_low in x)]
    cantidad=fran.shape[0]
    gananciat=fran['revenue'].sum()
    gananciap=fran['revenue'].mean()
    return {'franquicia':franquicia, 'cantidad':cantidad, 'ganancia_total':gananciat, 'ganancia_promedio':gananciap}





# API 4


def peliculas_pais(pais):
    p_low=pais.lower()
    cantidad = df['pcountry_name'].map(str.lower).apply(lambda x: p_low in x).sum()
    return {'pais': pais, 'cantidad': int(cantidad)}





# API 5


def productoras(productora):
    pprod=df[['pcompany_name','budget','revenue']].dropna()
    pprod['pcompany_name']=pprod['pcompany_name'].map(str.lower)
    pprod=pprod[pprod.pcompany_name.str.contains(productora.lower(), regex=False)]
    cantidad=pprod.shape[0]
    gtotal=pprod['revenue'].sum()
    return {'productora':productora, 'ganancia_total':gtotal, 'cantidad':cantidad}





# API 6


def retorno(pelicula):
    ppeli=df[['title','budget','revenue','return','release_year']].dropna()
    ppeli['title']=ppeli['title'].map(str.lower)
    ppeli=ppeli[ppeli['title']==str(pelicula).lower()]
    inver=ppeli['budget'].iloc[0]
    gan=ppeli['revenue'].iloc[0]
    ret=ppeli['return'].iloc[0]
    an=ppeli['release_year'].iloc[0]
    return {'pelicula':pelicula, 'inversion':int(inver), 'ganacia':int(gan),'retorno':int(ret), 'anio':int(an)}






