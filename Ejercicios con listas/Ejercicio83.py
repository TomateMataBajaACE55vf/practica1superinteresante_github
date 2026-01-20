#Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así sucesivamente. Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe algún método que permita sumar el contenido de una lista?
import random
sino="s"
puntuacion=[]
rondas=0
while sino in "Ss":
    rondas=rondas+1
    puntos=8
    adivinaadivinanza=""
    list1 = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
    topsecret=random.choice(list1)
    while adivinaadivinanza != topsecret:
        adivinaadivinanza=str(input("Introduce la palabra secreta: "))
        if adivinaadivinanza != topsecret:
            print("SIGUE JUGANDO")
            puntos=puntos-1
        else:
            print("ACERTASTE")
            puntuacion.append(puntos)
    sino=input("Deseas seguir jugando (s/n): ")
media=(8*rondas)/2
print("Puntuación: ",puntuacion)
print("Tu puntuación total ha sido: ",sum(puntuacion))
print("La media de partidas realizadas es: ",media)
if sum(puntuacion) > media:
    print("Corre a comprar la lotería.")
else:
    print("Mejor no entres en un casino.")