#A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40.
i=1
num=int(input("Introduce el número: "))
while i<11 and (i*num) <= 40:
    print(i*num)
    i=i+1
print("Fin de programa")