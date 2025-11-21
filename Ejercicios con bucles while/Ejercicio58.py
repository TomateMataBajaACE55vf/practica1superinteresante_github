#Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random
topsecret=random.randint(1,5)
intentos=int(0)
adivinaadivinanza=0
while intentos < 3:
    adivinaadivinanza=input("Introduce el número: ")
    if adivinaadivinanza.isnumeric():
        if int(adivinaadivinanza) == topsecret:
            print("Número acertado")
        else:
            print("Número no acertado")
    else:
        print("Eso no es un número entero")
    intentos=intentos+1