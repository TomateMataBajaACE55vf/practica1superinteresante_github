#Imprima el siguiente patrón con el ciclo for. 
patron="*"
pos=int(5)
for x in range(4):
    print(patron)
    patron=patron+"*"
for y in range(4):
    patron=patron.replace(str(pos),"")
    pos=pos-1
    print(patron)