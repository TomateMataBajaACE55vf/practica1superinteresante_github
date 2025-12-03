#Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo se comporta el dado en lanzamientos producidos durante aprox 3 segundos. 
import random
import time
uno=0
dos=0
tres=0
cuatro=0
cinco=0
seis=0
ahora=time.time()
while time.time() - ahora < 3:
    dado=random.randint(1,6)
    if dado==1:
        uno=uno+1
    if dado==2:
        dos=dos+1
    if dado==3:
        tres=tres+1
    if dado==4:
        cuatro=cuatro+1
    if dado==5:
        cinco=cinco+1
    if dado==6:
        seis=seis+1
print("Uno: ",uno)
print("Dos: ",dos)
print("Tres: ",tres)
print("Cuatro: ",cuatro)
print("Cinco: ",cinco)
print("Seis: ",seis)