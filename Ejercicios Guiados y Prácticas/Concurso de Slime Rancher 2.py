print("¡Bienvenido al concurso de preguntas sobre Slime Rancher 2!")
print("Empecemos con preguntas generales sobre las preferencias de nuestros amigos viscosos:")
res1=str(input("Cuál es la comida favorita del Slime Pescador?: "))
res1=res1.lower()
point=0
if "gallina de mar" in res1:
    print("¡Correcto!")
    point=point+1
else:
    print("Esa no era la respuesta correcta, su comida favorita es la Gallina de Mar.")
print("Has obtenido ",point,"puntos en total.")