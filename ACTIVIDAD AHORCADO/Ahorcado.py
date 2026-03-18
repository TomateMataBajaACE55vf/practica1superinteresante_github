import random
import time
from datetime import date, datetime
#lista de palabras secretas posibles
Lista_palabrasecreta=["palabra","zanguango","competitivo","obtuso","itinerario","longaniza","almendra","matadora","Benidorm","miranda"]
#variable para controlar si el usuario quiere seguir jugando
sino="s"
#listas para controlar las tildes y sus equivalentes sin tilde
tilde="áéíóú"
sinti="aeiou"
#bucle principal del juego mientras el usuario quiera continuar
while sino in "Ss":
    #se inicia el contador de tiempo
    tiempo1=time.perf_counter()
    #listas para guardar aciertos, errores y estado de la partida
    Lista_aciertos=[]
    Lista_errores=[]
    Lista_partida=[]
    #lista que representa el progreso del ahorcado
    Lista_ahorcado=["_","_","_","_","_","_","_","_"]
    #se elige una palabra secreta aleatoria y se elimina de la lista
    secret=str(random.choice(Lista_palabrasecreta))
    Lista_palabrasecreta.remove(secret)
    #se guarda la palabra original
    palabra=secret
    #se convierte la palabra en lista para trabajar mejor con sus posiciones
    secret=list(secret)
    #se inicializa la lista de la partida con guiones bajos
    for x in range(len(secret)):
        Lista_partida.append("_")
    #se muestra el estado inicial de la palabra
    print("[ "+ " , ".join(Lista_partida)+ " ]")
    #contador de errores inicializado en -1
    error=-1
    #bucle principal del juego hasta ganar o perder
    while Lista_ahorcado != ["A","H","O","R","C","A","D","O"] and Lista_partida != secret:
        pos=-1
        #se pide una letra al usuario
        letra=str(input("Introduce una letra: "))
        #se comprueba que la letra no haya sido usada antes
        while letra.lower() in Lista_errores or letra.upper() in Lista_errores or letra.lower() in Lista_aciertos or letra.upper() in Lista_aciertos:
            print("Esa letra ya la usaste.")
            letra=str(input("Introduce una letra: "))
        #se comprueba que lo introducido sea válido (una sola letra)
        while len(letra) != 1 and list(letra) != secret or letra.isalpha() == False:
            print("Lo que has introducido es incorrecto.")
            letra=str(input("Introduce una letra: "))
        #si el usuario introduce directamente la palabra completa
        if list(letra) == secret:
            Lista_partida=secret
            print("[ "+ " , ".join(Lista_partida)+ " ]")
        else:
            #se comprueba si la letra está en la palabra
            if letra.lower() in secret or letra.upper() in secret:
                #se recorre la palabra para sustituir las posiciones correctas
                for y in secret:
                    pos=pos+1
                    #si la letra tiene tilde se convierte a su equivalente sin tilde
                    if letra.lower() in tilde or letra.upper() in tilde:
                        letra=sinti[tilde.find(letra)]
                    #se hace lo mismo para comprobar coincidencias en diferentes formatos
                    if y == letra:
                        Lista_partida.pop(pos)
                        Lista_partida.insert(pos,y)
                    elif y == letra.lower():
                        Lista_partida.pop(pos)
                        Lista_partida.insert(pos,y)
                    elif y == letra.upper():
                        Lista_partida.pop(pos)
                        Lista_partida.insert(pos,y)
                    #se comprueba también el caso contrario (sin tilde a con tilde)
                    if letra in sinti:
                        letra2=tilde[sinti.find(letra)]
                        if y == letra2:
                            Lista_partida.pop(pos)
                            Lista_partida.insert(pos,y)
                        elif y == letra2.lower():
                            Lista_partida.pop(pos)
                            Lista_partida.insert(pos,y)
                        elif y == letra2.upper():
                            Lista_partida.pop(pos)
                            Lista_partida.insert(pos,y)
                        #se añade la letra con tilde a aciertos
                        Lista_aciertos.append(letra2)
                #se muestra el estado actualizado de la palabra
                print("[ "+ " , ".join(Lista_partida)+ " ]")
                #se añade la letra a la lista de aciertos
                Lista_aciertos.append(letra)
            else:
                #si la letra no está, se suma un error
                error=error+1
                #se actualiza el estado del ahorcado
                Lista_ahorcado.pop(error)
                Lista_ahorcado.insert(error,["A","H","O","R","C","A","D","O"][error])
                #se muestra el progreso del ahorcado
                print(*Lista_ahorcado)
                #se añade la letra a errores
                Lista_errores.append(letra)
    #se muestra la palabra secreta al finalizar
    print("La palabra era",palabra)
    #se calcula el tiempo total de la partida
    tiempo2=time.perf_counter()
    #se muestran aciertos y errores
    print("Aciertos:",len(Lista_aciertos))
    print("Errores:",len(Lista_errores))
    #se calcula el tiempo en segundos y minutos
    stotal=round(tiempo2-tiempo1,0)
    mtotal=0
    while stotal > 60:
        mtotal=mtotal+1
        stotal=stotal-60
    #se abre el archivo para guardar la partida
    txt=open("Partidas.txt", "a", encoding="utf-8")
    #se obtiene la fecha actual
    hoy=date.today()
    fecha=hoy.strftime("%d/%m/%Y")
    #se obtiene la hora actual
    hora=datetime.now()
    hora=hora.strftime('%H:%M')
    #se escriben los datos de la partida en el archivo
    txt.write("Fecha de la partida: "+fecha+"\n")
    txt.write("Hora de la partida: "+hora+"\n")
    txt.write("Palabra secreta: "+palabra+"\n")
    txt.write("Número de aciertos: "+str(len(Lista_aciertos))+"\n")
    txt.write("Número de errores: "+str(len(Lista_errores))+"\n")
    #se cierra el archivo
    txt.close()
    #se muestra el tiempo utilizado
    print(f"Tiempo utilizado: {mtotal} minutos y {int(stotal)} segundos")
    #se pregunta al usuario si quiere añadir una nueva palabra
    nosi=input("¿Deseas añadir una palabra? (s/n): ")
    #se valida la respuesta
    while nosi not in "Ss" and nosi not in "Nn" or nosi.isalpha() == False:
        print("Respuesta incorrecta.")
        nosi=input("¿Deseas añadir una palabra? (s/n): ")
    #si el usuario quiere añadir palabra
    if nosi in "Ss":
        nuevo=input("Introduce la palabra: ")
        #se comprueba que la palabra sea válida
        while nuevo.isalpha() == False:
            print("Respuesta incorrecta.")
            nuevo=input("Introduce la palabra: ")
        #se añade la nueva palabra a la lista
        Lista_palabrasecreta.append(nuevo)
    #se pregunta si quiere continuar jugando
    sino=input("¿Deseas continuar? (s/n): ")
    #se valida la respuesta
    while sino not in "Ss" and sino not in "Nn" or sino.isalpha() == False:
        print("Respuesta incorrecta.")
        sino=input("¿Deseas continuar? (s/n): ")