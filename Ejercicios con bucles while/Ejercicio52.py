#Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While
op1=int(input("Introduce un número entero: "))
op2=int(input("Introduce otro número entero: "))

suma=op1+op2

print("El resultado de la suma es: ", suma)

sino=str(input("Deseas repetir la operación s/n: "))

while sino=="s":
    op1=int(input("Introduce un número entero: "))
    op2=int(input("Introduce otro número entero: "))

    suma=op1+op2

    print("El resultado de la suma es: ", suma)

    sino=str(input("Deseas repetir la operación s/n: "))
print("Programa finalizado")