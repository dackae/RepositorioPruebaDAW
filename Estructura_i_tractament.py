#Precondició: L'usuari té l'informació necessaria per omplir els requeriments el programa
#constants
alumnes="Indica la quantitat d'alumnes que vols registrar "
dades="Introdueix les seguents dades de l'alumne separades per espais: Nom, Cognom, Edat, Nota1, Nota2, Nota3: "
titol_llista2="1 o més notes majors que 8"
titol_llista1="Mitjana superior a 7"
#endconstants
#var
condicion_lista=False
suma=0
n=0
nota1
nota2
nota3
lista1=[]
lista2=[]
x=int(input(alumnes))
#endvar
for i in range(0,x):
    dades_alumne=input(dades)
    dades_alumne=dades_alumne.split(" ")
    notas=[float(dades_alumne[3])]
    notas.append(float(dades_alumne[4]))
    notas.append(float(dades_alumne[5]))
    tupla=(dades_alumne)
    nota1=nota[0]*0,3
    nota2=nota[1]*0,4
    nota3=nota[2]*0,3
    notafinal=nota1+nota2+nota3
    if notafinal>7:
        lista1.append(tupla)
    if notas[0]>8:
        lista2.append(tupla)
    if notas[1]>8:
        lista2.append(tupla)
    if notas[2]>8:
        lista2.append(tupla)
if len(lista1)>0:
    i=0
    print(titol_llista1, "\n")
    while condicion_lista==False:
        print("\t", lista1[i])
        i+=1
        if i>=len(lista1):
            condicion_lista=True
else:
    print("Ningun alumne ha obtingut una mitjana superior a 7")   
if len(lista2)>0:
    i=0
    condicion_lista=False
    print(titol_llista2, "\n")
    while condicion_lista==False:
        print("\t", lista2[i])
        i+=1
        if i>=len(lista2):
            condicion_lista=True
else:
    print("Ningun alumne ha obtingut una nota superior a 8")
#Postcondició: El programa retorna dues llistes amb els alumnes segons quina condició compleixen