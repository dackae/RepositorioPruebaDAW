#PRE:
#Juego de preguntas (en catalan))
import random
continuar=True
dic_capitales={'Bosnia y Hezergovina' : 'Sarajevo', 'España' : 'Madrid', 'Francia' : 'Paris', 'Alemania' : 'Berlín', 'Reino Unido' : 'Londres', 'Argelia' : 'Argel', 'Kenia' : 'Nairobi', 'Madagascar' : 'Antananarivo', 'India' :'Nueva Deli'}
lista_claves=list(dic_capitales.keys())
print("Si quieres dejar de responder preguntas, di 'stop'")
puntuacion=0
while continuar==True:
    pais_pregunta= random.choice(lista_claves)
    respuesta=str(input('Dime la capital de '+pais_pregunta+': '))
    if respuesta.lower()== 'stop':
        continuar=False
    if respuesta.lower() == dic_capitales[pais_pregunta].lower():
        puntuacion+=1
print('Esta es tu puntuación: ', puntuacion)