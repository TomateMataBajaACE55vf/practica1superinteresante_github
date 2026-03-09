lista=input()
lista=lista.split("-")
prods=[]
precs=[]
stock=[]
for x in range(len(lista)):
    info=lista[x].split(":")
    prods.append(info[0])
    precs.append(info[1])
    stock.append(info[2])
valor_total=0
for y in range(len(prods)):
    valor_total+=float(precs[y])*float(stock[y])
print("Valor total del inventario:",valor_total)
max_precio=max(precs)
pos=precs.index(max_precio)
print("Producto más caro:", prods[pos])
print("Productos con stock 0:")
for z in range(len(prods)):
    if float(stock[z]) == 0:
        print(prods[z])
prod=float(0)
while prod < len(prods):
    if float(stock[int(prod)]) == 0:
        prods.pop(int(prod))
        precs.pop(int(prod))
        stock.pop(int(prod))
    else:
        prod+=1
print("Resumen final:")
for a in range(len(prods)):
    print(prods[a], precs[a], stock[a])