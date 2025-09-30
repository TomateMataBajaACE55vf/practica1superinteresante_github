#Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
var1=float(input("Introduce un número: "))
if 0 <= var1 <=10:
    if var1 >= 5:
        print("Has sacado un",var1," has aprobado.")
    elif var1 < 5:
        print("Has sacado un",var1," has suspendido.")
else:
    print("La nota que has introducido no está entre 0 y 10.")