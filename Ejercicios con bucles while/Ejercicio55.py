#Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
op1=int(input("Introduce un número entero: "))
op2=int(input("Introduce otro número entero: "))

suma=op1+op2
sumdef=int(0)

print("El resultado de la suma es: ", suma)
sumdef=sumdef+suma
repe=int(1)
print(f"El total acumulado es: {sumdef} y llevas {repe} operación realizada.")
#mientras se cumpla una de las dos condiciones se repetirá
while sumdef < 51 or sumdef%2 == 0:
    op1=int(input("Introduce un número entero: "))
    op2=int(input("Introduce otro número entero: "))

    suma=op1+op2
    sumdef=sumdef+suma
    print("El resultado de la suma es: ", suma)
    print(f"El total acumulado es: {sumdef} y llevas {repe} operaciones realizadas.")
    repe=repe+1
print("Fin del programa")