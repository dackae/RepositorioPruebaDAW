#Pre:L'usuari no utilitzara caracters especials apart de la , o el .
text=input("Introdueix el text: ")
text=text.lower()
text=text.split(",")
text="".join(text)
text=text.split(".")
text="".join(text)
text=text.split(" ")
dic_recuento={}
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
     dic_recuento[text[i]]=cont
     i+=1
     if i>=len(text):
          condicion_texto=True
lista_palabras=list(dic_recuento.keys())
lista_cantidad=list(dic_recuento.values())
k=0
x=0
fin=False
celdas=len(lista_cantidad)
while fin!=True:
     for k in range(0,len(lista_cantidad)-1-x):
          if lista_cantidad[k]<lista_cantidad[k+1]:
               lista_cantidad[k], lista_cantidad[k+1]= lista_cantidad[k+1], lista_cantidad[k]
               lista_palabras[k], lista_palabras[k+1]= lista_palabras[k+1], lista_palabras[k]
          
     x+=1
     if x==len(lista_cantidad)-1:
          fin=True
for k in range(0,len(lista_cantidad)):
     print(lista_palabras[k], '=', lista_cantidad[k])
#Post: Per pantall es mostra a l'esquerra la paraula i a la dreta del "=" la quantitat de cops que apareix ordenat de major a menor.