#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
var1=int(input("Introduce un número: "))
var2=int(input("Introduce otro número: "))
#Para ver si más de 1 cosa se cumple se usa "and".
if 0 <= var1 <=10 and 0 <= var2 <= 10:
    if var1 > var2:
        print("El número ",var1," es mayor que el número ",var2,".")
    elif var1 < var2:
        print("El número ",var2," es mayor que el número ",var1,".")
    else:
        print("Ambos números son iguales.")
else:
    print("Uno o los dos números están fuera de los límites establecidos.")