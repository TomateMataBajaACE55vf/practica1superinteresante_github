#A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While
op1=int(input("Introduce un número entero: "))
op2=int(input("Introduce otro número entero: "))

suma=op1+op2
sumdef=int(0)

print("El resultado de la suma es: ", suma)
sumdef=sumdef+suma
sino=str(input("Deseas repetir la operación s/n: "))
repe=int(1)
while sino=="s":
    op1=int(input("Introduce un número entero: "))
    op2=int(input("Introduce otro número entero: "))

    suma=op1+op2
    sumdef=sumdef+suma
    print("El resultado de la suma es: ", suma)

    sino=str(input("Deseas repetir la operación s/n: "))
    repe=repe+1
print("Resumen")
print(f"La suma total es: {sumdef} y el número de repeticiones es: {repe}")