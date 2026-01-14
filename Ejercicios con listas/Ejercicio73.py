#Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no
list1=["casa","mesa","sal","sol","agua"]
list2=["casa","luz","tres","tren","sol","pan"]
list3=[]
list4=[]
for word in list2:
    if word in list1:
        list3.append(word)
    else:
        list4.append(word)
list3=list(set(list3))
list4=list(set(list4))
print("Están repetidas: ",list3)
print("No están repetidas: ",list4)