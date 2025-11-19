#Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural.. . Con While
op1=int(input("Introduce un número entero: "))
op2=int(input("Introduce otro número entero: "))

suma=op1+op2
sumdef=int(0)

print("El resultado de la suma es: ", suma)
sumdef=sumdef+suma
repe=int(1)
print(f"El total acumulado es: {sumdef} y llevas {repe} operación realizada.")
while sumdef < 51:
    op1=int(input("Introduce un número entero: "))
    op2=int(input("Introduce otro número entero: "))

    suma=op1+op2
    sumdef=sumdef+suma
    print("El resultado de la suma es: ", suma)
    print(f"El total acumulado es: {sumdef} y llevas {repe} operaciones realizadas.")
    repe=repe+1
print("Fin del programa")