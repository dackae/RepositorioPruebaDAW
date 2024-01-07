#Pre:
text=input("Introdueix el text: ")
text=text.lower()
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
#para el bubble sort voy a pillar el diccionario y voy a hacer dos listas
#una con las keys la otra lso values
#comparo values y reordeno los values a la vez que las keys
#luego creo un bucle para añadir indice 1 de uno e indice 1 del otro en una variable algo al estilo:
# variable= palabra(lista_palabras)'=' numero(lista_cantidad)