#Imprime el siguiente patrón utilizando for:
patron="54321"
pos=int(5)
for x in range(5):
    print(patron)
    #reemplazamos la posición indicada por un espacio
    patron=patron.replace(str(pos),"")
    pos=pos-1