#Utilizando listas, crea un programa que te permita determinar si un número es decimal o no. 
num=input("Introduce un número: ")
list1=list(num)
dec=0
for pos in list1:
    if pos == ".":
        dec=dec+1
    elif pos.isnumeric() == False:
        dec=dec+2
if dec == 1:
    print("Es un número con decimales")
else:
    print("No es un número con decimales")