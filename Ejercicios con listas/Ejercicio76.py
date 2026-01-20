#A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.
list1=["a","b","D","x","r","X","3","h","w","2","i"]
list2=[]
list3=[]
for pos in list1:
    if pos.isnumeric():
        list2.append(pos)
    elif pos.isalpha():
        list3.append(pos)
mayusminus=int(input("Introduce 1 para visualizar en orden ascendente o 2 descendente: "))
if mayusminus == 1:
    list2.sort(key=str.lower)
    list3.sort(key=str.lower)
else:
    list2.sort(reverse=True,key=str.lower)
    list3.sort(reverse=True,key=str.lower)
print(list2)
print(list3)
    