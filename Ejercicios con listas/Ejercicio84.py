#A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 
import random
tries=0
list1 = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
secret=random.choice(list1)
topsecret=list(secret)
random.shuffle(topsecret)
print(topsecret)
resp=""
while resp != secret and tries < 3:
    resp=str(input("Introduce la palabra correcta: "))
    if resp != secret:
        print("No has acertado")
        tries=tries+1
    else:
        print("Acertaste")
if tries == 3:
    print("No has acertado ninguno de los intentos")