milista=[1,2,3,4,5,6]
milistapor2=[]
maximo=max(milista)
minimo=min(milista)
suma=sum(milista)

for pos in milista:
    num2=pos*2
    milistapor2.append(num2)

print(milista)
print("Máximo: ",maximo)
print("Mínimo: ",minimo)
print("Suma total: ",suma)
print(milistapor2)