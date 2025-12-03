#Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número de veces que se repite cada número.
import random
uno=0
dos=0
tres=0
cuatro=0
cinco=0
seis=0
for x in range(100):
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
