#Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos.
import random
topsecret=random.randint(0,1000)
intentos=int(0)
adivinaadivinanza=1000000000
while int(adivinaadivinanza) != topsecret:
    adivinaadivinanza=input("Introduce el número: ")
    if adivinaadivinanza.isnumeric():
        if int(adivinaadivinanza) > topsecret:
            print("El número que has introducido es mayor")
        elif int(adivinaadivinanza) < topsecret:
            print("El número que has introducido es menor")
    else:
        print("Eso no es un número entero")
    intentos=intentos+1
print(f"Acertaste, has realizado {intentos} intentos")