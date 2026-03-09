lista=input()
lista=lista.split(",")
print(lista)
max=float(lista[0])
min=float(lista[0])
for x in range(len(lista)):
    if int(lista[x]) > int(max):
        max=lista[x]
    if int(lista[x]) < int(min):
        min=lista[x]
lista.remove(min)
lista.remove(max)
print(lista)
listaf=[]
for x in range(len(lista)):
    listaf.append(float(lista[x]))
media=float(round(sum(listaf)/len(listaf),2))
if media < 5:
    print("Rendimiento bajo")
elif media > 10:
    print("Rendimiento alto")
else:
    print("Rendimiento medio")