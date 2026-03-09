long=int(input())
lista=[]
for x in range(long):
    a=int(input())
    lista.append(a)
max=lista[0]
min=lista[0]
for x in range(len(lista)):
    if int(lista[x]) > int(max):
        max=lista[x]
    elif int(lista[x]) < int(min):
        min=lista[x]
if max-min in lista:
    print(":)")
else:
    print(":(")