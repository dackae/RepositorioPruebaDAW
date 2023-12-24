#Pre:
text=input("Introdueix el text: ")
text=text.casefold()
text=text.split(",")
text="".join(text)
text=text.split(".")
text="".join(text)
text=text.split(" ")
dic={}
condicion_texto=False
i=0
while condicion_texto==False:
     cont=1
     j=0
     while j < len(text):
          if text[i]==text[j] and i!=j:
               del text[j]
               cont+=1
          else:
               j+=1
     dic[text[i]]=cont
     i+=1
     if i>=len(text):
          condicion_texto=True
print(dic)
#Lo que debo hacer seria mas o menos el comparar indice i i indice j si son iguales aumento en 1 el contador y a la vez borro el indice actual, nota, hacerlo en un while para no aumentar la j en caso de que borre el j
#Lo del diccionario esta bien
#Post:a