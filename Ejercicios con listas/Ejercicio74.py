#A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas.
list1=["casa","mesa","sal","sol","agua"]
list2=["casa","luz","tres","tren","sol","pan"]
list3=[]
list5=[]
for word1 in list1:
    for word2 in list2:
        if word1 == word2:
            list3.append(word2)
print("Están repetidas: ",list3)
list4=list1+list2
for word3 in list4:
    if word3 not in list3:
        list5.append(word3)
print("No están repetidas: ",list5)