#Precondició: L'usuari té l'informació necessaria per omplir els requeriments el programa
#constants
alumnes="Indica la quantitat d'alumnes que vols registrar "
dades="Introdueix les seguents dades de l'alumne separades per espais: Nom, Cognom, Edat, Nota1, Nota2, Nota3: "
#endconstants
#var
i=0
lista1=[]
lista2=[]
x=int(input(alumnes))
a="tal tal tal 1 2 6"
text=a.split(" ")
#endvar
while i < x:
    dades_alumne=input(dades)
    dades_alumne=dades_alumne.split(" ")
    notas=[int(dades_alumne[3])]
    notas.append(int(dades_alumne[4]))
    notas.append(int(dades_alumne[5]))
    print(notas)
    tupla=(dades_alumne, notas)
    if notas[0]>8:
        lista1.append(tupla)
        print("bien")
    if notas[1]>8:
        lista1.append(tupla)
        print("bien")
    if notas[2]>8:
        lista1.append(tupla)
        print("bien")
    i+=1

#Postcondició: El programa retorna dues llistes amb els alumnes segons quina condició compleixen