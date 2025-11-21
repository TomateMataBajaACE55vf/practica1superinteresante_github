#Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
topsecret=random.randint(1,5)
adivinaadivinanza=input("Introduce el número: ")
if adivinaadivinanza.isnumeric():
    if int(adivinaadivinanza) == topsecret:
        print("Número acertado")
    else:
        print("Número no acertado")
else:
    print("Eso no es un número entero")