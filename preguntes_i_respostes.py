#PRE:
#Juego de preguntas (en catalan))
dic_capitales={'Bosnia y Hezergovina' : 'Sarajevo', 'España' : 'Madrid', 'Francia' : 'Paris', 'Alemania' : 'Berlín', 'Reino Unido' : 'Londres', 'Argelia' : 'Argel', 'Kenia' : 'Nairobi', 'Madagascar' : 'Antananarivo', 'India' :'Nueva Deli'}
seed= 2
seed= (seed*997) % 1000
random= (seed*503) % 1000 / 100
numero_pregunta= int(random * (len(dic_capitales)))
lista_claves=list(dic_capitales.keys())
print(lista_claves[numero_pregunta])
