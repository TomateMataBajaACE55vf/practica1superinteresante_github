#Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine la palabra
import random
adivinaadivinanza=""
list1 = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
topsecret=random.choice(list1)
while adivinaadivinanza != topsecret:
    adivinaadivinanza=str(input("Introduce la palabra secreta: "))
    if adivinaadivinanza != topsecret:
        print("SIGUE JUGANDO")
    else:
        print("ACERTASTE")