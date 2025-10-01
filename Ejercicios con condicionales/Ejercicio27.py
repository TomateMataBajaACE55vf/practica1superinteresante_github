#Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla.
letra=str(input("Introduce una letra: "))

if (letra.isupper()):
    print("La letra es mayúscula.")
if (letra.islower()):
    print("La letra es minúscula.")
if (letra.isnumeric()):
    print("El valor introducido es un número.")
