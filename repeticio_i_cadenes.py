#Pre:
text=input("Introdueix el text")
text.casefold()
text.split(" ")
text_aux=text
dic={}
cont=0
i=0
while condicion_texto==False:
    cont=0
    salida=False
    while salida==False:
        if text.find(text[i])==-1:
            salida=True
        else:
            cont+=1
            del text[text.find(text[i])]
    dic[text[i]:cont]
    del text[i]
    i+=1
    if i==len(text):
        condicion_texto=True
#Post:a