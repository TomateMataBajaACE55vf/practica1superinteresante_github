import time
print("¡Bienvenido al concurso de preguntas sobre Brawl Stars!")
time.sleep(3)
sino="s"
while sino == "s":
    print("Empecemos con preguntas generales:")
    time.sleep(3)
    res1=str(input("¿Cuál es la comida favorita de Mortis?: "))
    res1=res1.lower()
    point=0
    if "" in res1:
        print("¡Correcto!")
        point=point+1
    else:
        print("Esa no era la respuesta correcta, su comida favorita son los muros.")
    time.sleep(3)
    res2=str(input("¿Cómo se llama el recurso con el que se desbloquean brawlers?: "))
    res2=res2.lower()
    if "créditos" in res2 or "creditos" in res2:
        print("¡Correcto!")
        point=point+1
    else:
        print("Esa no era la respuesta correcta, el recurso son los créditos.")
    time.sleep(3)
    res3=str(input("¿Cuál es la habilidad que se activa con un botón morado?: "))
    res3=res3.lower()
    if "hipercarga" in res3:
        print("¡Correcto!")
        point=point+1
    else:
        print("Esa no era la respuesta correcta, la habilidad es la hipercarga.")
    time.sleep(3)
    print("¡Ahora sigamos con nombres!")
    time.sleep(3)
    res4=str(input("¿Cómo se llaman las notas de Melodie?: "))
    res4=res4.lower()
    if "chichi" in res4 and "yoyo" in res4:
        print("¡Correcto!")
        point=point+1
    else:
        print("Esa no era la respuesta correcta, las notas que acompañan a Melodie se llaman Chichi y Yoyo.")
    time.sleep(3)
    res5=str(input("¿Cuál es el único brawler que se quedó sin hipercarga entre noviembre y diciembre de 2025?: "))
    res5=res5.lower()
    if "gigi" in res5:
        print("¡Correcto!")
        point=point+1
    else:
        print("Esa no era la respuesta correcta, ese brawler fue Gigi.")
    time.sleep(3)
    print("Has obtenido ",point,"puntos en total.")
    time.sleep(5)
    sino=str(input("¿Deseas intentar de nuevo?(s/n): "))