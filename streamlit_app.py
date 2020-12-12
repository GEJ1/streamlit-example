from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import numpy as np
from os import path
import requests


"""
# Probando!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

texto = " Porque me gustaría aprender este tipo de lenguaje, del cual no tengo conocimientos, 
porque se que es importante Me interesa conocer la base de programación en phyton para a futuro 
poder aplicarlo a investigación en psicología  Quisiera aprender a manejar la herramienta y me 
interesa ver una articulación entre programación y psicología. Conocer python Me parece importante 
tener conocimientos de lenguajes de programación Porque va permitir formarnos en al algo que lamentablemente 
no se suele ver en la carrera, y considero que es una herramienta necesaria que nos va  ayudar, por ejemplo, 
en el desarrollo de futuras investigaciones.  Porque me parece útil para mi carrera  Quiero aprender programación
para poder aplicar esos conocimientos en el futuro Me interesa programación. Para investigación es muy 
importante saber programar  Amo Python!! Y estoy donde ustedes estén!! 
Quiero empezar a volcarme hacia la investigación y de que estos son temas  
fundamentales Me interesa la programación y como aplicarla a la psicología en 
un futuro Soy becaria de investigación y trabajo con spss, pero creo que tengo 
que migrar a otros programas.  Hace tiempo ya me interesa empezar a adentrarme 
en el uso de este programa Después de la charla que dieron sobre data sciencie me 
interesó conocer su posible aplicación en la psicología. Pero es algo ajeno a mi conocimiento, 
por lo que me beneficiaría tener alguna introducción   Me resulta súper interesante la propuesta 
y quiero aprender e interiorizarme en el tema! quiero programar Para tener más herramientas a la 
hora de insertarme en el área de investigación Para contribuir a mi formación Porque creo que me 
puede servir para la carrera Para adquirir más conocimientos en programación. Aprender las bases 
de utilización de Phyton para el análisis de datos. Para aprender  Quiero empezar a aprender sobre 
programación ya que puede ser útil para cuando me dediqué a la investigación  
Aprender de programación puede ser de utilidad en mi carrera Me interesa la investigación 
en psico  Quiero aprender a aplicar la estadística a la psicología  Porque me parece necesario 
para investigar. Aprender :) Me interesa ser data scientist orientada a psico  Soy docente de 
    ingeniería biomédica también y quiero conocer esta tecnología que utilizan los alumnos  
    Porque cuando veo la metadata de una página siento que voy a ser reclutado por Anonymus. 
    Ah, y quiero usar programación para análisis de datos  Para practicar un poco. 
    Porque me interesa la programación  Me interesa tener más herramientas para en un 
    futuro poder hacer investigación. Aprender una herramienta Ingresar en el tema  
    Quiero aprender a aplicar la estadística a la psicología  Porque estoy por recibirme 
    y voy a comenzar a estudiar diseño de experiencia de usuario y me interesa saber sobre 
    análisis de datos.  Los 2 futuros profesionales que me interesan requieren que sepa programar 
    Me interesa la investigación y creo que es necesario aprender lenguajes de programación.  
    Me parece una buena oportunidad para aprender al menos lo básico de programación, ya que por ahora
    es un tema que tengo bastante flojo para aplicar a la investigación junto con la estadística 
    Quiero aprender a programar Para aprender sobre programación en relación con el análisis de 
    datos en psicología Para aprender programación Para interiorizarme un poco sobre programación 
    Porque en un futuro quiero dedicarme a la investigación y quiero aprender algo sobre programación,
    ya sea Python o R Estoy con muchas ganas de aprender a programar, pienso que puede darme más posibilidades 
    de competir por un trabajo en el futuro Asistí al taller que dieron en el Congreso de este año y 
    quisiera aprender a utilizar Python Me interesa la programación como una parte del presente y el 
    futuro de la Psicología! Quiero saber algo de programación Me parece una buena herramienta que la 
    curricula obligatoria no te brinda  Python es un programa que me interesa mucho Quiero conocer otra 
    forma de hacer análisis estadístico diferentes a SPSS Es necesario abrir las ciencias sociales y acercarnos 
    a espacios interdisciplinarios para devenir en categorías otras que den razón de lo que sucede . 
    La programacion es la base del presente futuro considero necesario este conocimiento Me interesa aprender
    a programar porque se esta convirtiendo en una cuestión basica para muchos empleos Hace rato quiero formarme 
    en programacion, en como realizar meta analisis etc y me parece una buena forma para arrancar y tener una 
    herramienta más para investigar Para adquirir conocimiento sobre herramientas google Quiero aprender 
    Ampliar conocimientos Porque veo que muchxs hablan del tema y no conozco NADA Me interesa conocer cómo 
    se aplica Python a la ciencia de datos y más que nada comprender cómo es el proceso de análisis de datos. 
    Porque considero que la tecnología es un factor clave para ejercer mi futura profesión, gracias por la propuesta! 
    Me interesa aprender a analizar datos en Python y saber qué cosas puedo hacer con Google Colab  
    Creo que es muy útil este taller, tener conocimientos sobre python y como utilizarlo  En este momento 
    estoy haciendo un curso parte del plan Argentina Programa.  Me parece una herramienta util como nueva 
    metodologia de analisis Porque me gusta hacer talleres y aprender todo actualizado Para adquirir 
    conocimientos desde cero  Me interesa para mi tesis Me interesa adquirir conocimientos al respecto 
    aprender herramientas para investigar Todo esto se aplica en los test y diversos asuntos que se 
    resuelven a través de esto interés Me gustaría aprender más sobre Python para análisis de datos, ya que conozco sobre R. 
    Quiero aprender a programar ya que actualmente estoy por comenzar el doctorado en psicología y creo que me va 
    a servir para mí tesis  Para adquirir herramientas y conocimiento  Para aplicar el conocimiento y las 
    herramientas en investigación y en proyectos de People Analytics  Quiero dedicarme a la psicología 
    cognitiva experimental y necesito formarme en programación 
Por que la gente que lo da es muy crack y me vendría bien para la tesis. Para aprender más sobre el tema  Para usar programas de investigacion "

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
