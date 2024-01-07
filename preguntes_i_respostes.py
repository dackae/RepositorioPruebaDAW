#PRE:
#Juego de preguntas (en catalan))
import random
dic_capitales={'Bosnia y Hezergovina' : 'Sarajevo', 'España' : 'Madrid', 'Francia' : 'Paris', 'Alemania' : 'Berlín', 'Reino Unido' : 'Londres', 'Argelia' : 'Argel', 'Kenia' : 'Nairobi', 'Madagascar' : 'Antananarivo', 'India' :'Nueva Deli'}
lista_claves=list(dic_capitales.keys())
pais_pregunta= random.choice(lista_claves)
respuesta=str(INPUT(print('Dime la capital de', pais_pregunta)))
