#A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.
list1=["a","b","D","x","r","X","3","h","w","2","i"]
list2=[]
list3=[]
for pos in list1:
    if pos.isnumeric():
        list2.append(pos)
    elif pos.isalpha():
        list3.append(pos)
list2=list2.sort()
list3=list3.sort()
print(list2)
print(list3)
    