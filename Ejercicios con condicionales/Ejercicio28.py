#Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.
letra=str(input("Introduce una letra: "))

if (letra.isupper()):
    print("La letra es mayúscula.")
elif (letra.islower()):
    print("La letra es minúscula.")
elif (letra.isnumeric()):
    print("El valor introducido es un número.")
else:
    print("El valor introducido es un símbolo.")