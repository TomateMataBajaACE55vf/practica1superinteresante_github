import time
print("¡Bienvenido al concurso de preguntas sobre Slime Rancher 2!")
time.sleep(3)
print("Empecemos con preguntas generales sobre las preferencias de nuestros amigos viscosos:")
time.sleep(3)
res1=str(input("Cuál es la comida favorita del Slime Aleteo?: "))
res1=res1.lower()
point=0
if "néctar rocío de luna" in res1:
    print("¡Correcto!")
    point=point+1
else:
    print("Esa no era la respuesta correcta, su comida favorita es el Néctar Rocío de Luna.")
res2=str(input("De qué slime es favorito la Polariguinda?: "))
res2=res2.lower()
if "gemelo" in res2:
    print("¡Correcto!")
    point=point+1
else:
    print("Esa no era la respuesta correcta, el slime cuyo favorito es la Polariguinda es el Slime Gemelo.")
res3=str(input("De qué slime es favorito el juguete del Bote de Basura?: "))
res3=res3.lower()
if "colianillado" in res3:
    print("¡Correcto!")
    point=point+1
else:
    print("Esa no era la respuesta correcta, el slime cuyo juguete favorito es el Bote de Basura es el Slime Colianillado.")
print("Has obtenido ",point,"puntos en total.")