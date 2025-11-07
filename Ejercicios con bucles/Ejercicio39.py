#Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.
posi=int(0)
nega=int(0)
cero=int(0)
numnum=int(input("Introduce la cantidad de números que deseas introducir: "))
for x in range(numnum):
    num=float(input("Introduce un número: "))
    if num > 0:
        posi=posi+1
    elif num < 0:
        nega=nega+1
    else:
        cero=cero+1
print("La cantidad de números positivos es: ",posi)
print("La cantidad de números negativos es: ",nega)
print("La cantidad de números ceros es: ",cero)