array = ["indigo", "groc", "verd", "vermell", "blau", "cian", "taronja"]

#colors_ordenats=["indigo", "blau", "cian", "verd", "groc", "taronja", "rojo"]
colors={'indigo' : 420, 'blau' : 460, 'cian' : 489, 'verd' : 495, 'groc' : 574, 'taronja' : 595, 'vermell' : 619}
ordenat=False
contador=len(array)-1
while contador>0:
  for i in range(0, len(array)-1):
    if array[i] > array[i+1]:
      aux=array[i+1]
      array[i+1]=array[i]
      array[i]=aux
  contador-=1
print(array)