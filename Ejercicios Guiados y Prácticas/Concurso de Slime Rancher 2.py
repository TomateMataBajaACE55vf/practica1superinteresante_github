import time
print("¡Bienvenido al concurso de preguntas sobre Slime Rancher 2!")
time.sleep(3)
if "si" or "sí" in vaj:

print("Empecemos con preguntas generales sobre las preferencias de nuestros amigos viscosos:")
time.sleep(3)
res1=str(input("¿Cuál es la comida favorita del Slime Aleteo?: "))
res1=res1.lower()
point=0
if "néctar rocío de luna" in res1:
    print("¡Correcto!")
    point=point+1
else:
    print("Esa no era la respuesta correcta, su comida favorita es el Néctar Rocío de Luna.")
time.sleep(3)
res2=str(input("¿De qué slime es favorito la Polariguinda?: "))
res2=res2.lower()
if "gemelo" in res2:
    print("¡Correcto!")
    point=point+1
else:
    print("Esa no era la respuesta correcta, el slime cuyo favorito es la Polariguinda es el Slime Gemelo.")
time.sleep(3)
res3=str(input("¿De qué slime es favorito el juguete del Bote de Basura?: "))
res3=res3.lower()
if "colianillado" in res3:
    print("¡Correcto!")
    point=point+1
else:
    print("Esa no era la respuesta correcta, el slime cuyo juguete favorito es el Bote de Basura es el Slime Colianillado.")
time.sleep(3)
print("¡Ahora sigamos con Spawn Rates!")
time.sleep(3)
res4=str(input("¿Cuál es el slime que aparece en un evento de tornado?: "))
res4=res4.lower()
if "derviche" in res4:
    print("¡Correcto!")
    point=point+1
else:
    print("Esa no era la respuesta correcta, el slime que aparece en un tornado es el Slime Derviche.")
time.sleep(3)
res5=str(input("¿Cuál es el slime más raro del juego?: "))
res5=res5.lower()
if "yema" in res5:
    print("¡Correcto!")
    point=point+1
else:
    print("Esa no era la respuesta correcta, el slime más raro del juego es el Slime Yema.")
time.sleep(3)
res6=str(input("¿Cuál es el gordo que tapa la entrada al portal del laberinto que te lleva a Lava Dephts?: "))
res6=res6.lower()
if "búm" in res6:
    print("¡Correcto!")
    point=point+1
elif "bum" in res6:
    print("Está súper híper mega mal escrito pero bueno, por alguna extraña razón el juego lo categoriza como Búm.")
    point=point+1
else:
    print("Esa no era la respuesta correcta, el gordo es el gordo Búm.")
time.sleep(3)
print("¡Sigamos con un poco de personajes principales!")
res7=str(input("¿Qué personaje del intercambio de pradera te da los portales?: "))
res7=res7.lower()
if "víktor" in res7:
    print("¡Correcto!")
    point=point+1
else:
    print("Esa no era la respuesta correcta, el personaje es Víktor Humphries.")
time.sleep(3)
res8=str(input("¿Quién es la persona que mandó la carta al principio del juego?: "))
res8=res8.lower()
if "gigi" in res8:
    print("¡Correcto!")
    point=point+1
else:
    print("Esa no era la respuesta correcta, la persona es Gigi Twillgers.")
time.sleep(3)
print("¡Terminamos con curiosidades!")
res9=str(input("¿Cuál es el plort que más carga a los drones?: "))
res9=res9.lower()
if "dorado" in res9:
    print("¡Correcto!")
    point=point+1
else:
    print("Esa no era la respuesta correcta, el plort era el plort Dorado.")
time.sleep(3)
res10=str(input("¿Cuál es el gordo que es el único en su zona?: "))
res10=res10.lower()
if "sable" in res10:
    print("¡Correcto!")
    point=point+1
else:
    print("Esa no era la respuesta correcta, el único gordo de Acantilados Polvorosos es el gordo Sable.")
time.sleep(3)
print("Has obtenido ",point,"puntos en total.")
time.sleep(5)