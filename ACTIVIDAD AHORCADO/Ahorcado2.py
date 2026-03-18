import random
import time
from datetime import date, datetime
#lista de palabras secretas posibles (ampliada respecto a la versión anterior)
Lista_palabrasecreta=["palabra","zanguango","competitivo","obtuso","itinerario","longaniza","almendra","matadora","Benidorm","miranda","polítoton","polimerasa","argón","enriquecer","oposición","llanura","Vetusta","ununennio","apoteósico","efervescente","ultratumba"]
#variable para controlar si el usuario quiere seguir jugando
sino="s"
#listas para controlar las tildes y sus equivalentes sin tilde
tilde="áéíóú"
sinti="aeiou"
#variables para el sistema de puntos y tienda
puntos=0
com1=0
com2=0
por2=0
por3=0
por4=0
por5=0
dicc="No"
dicsino="N"
dicactivado=0
#bucle principal del juego mientras el usuario quiera continuar
while sino in "Ss":
    #se inicializa el multiplicador y control de uso de vocales
    mult=float(1)
    vocaluso=float(0)
    #si se ha comprado el modo diccionario se pregunta si activarlo
    if dicc == "Sí":
        dicsino=input("¿Deseas activar el modo diccionario? (s/n): ")
        while dicsino not in "Ss" and dicsino not in "Nn" or dicsino.isalpha() == False:
            print("Respuesta incorrecta.")
            dicsino=input("¿Deseas activar el modo diccionario? (s/n): ")
    #si se activa el modo diccionario se carga el archivo
    if dicsino in "Ss":
        if float(dicactivado) == 0:
            dic=open("Diccionario.txt", "r", encoding="utf-8")
            dic=dic.read().splitlines()
            dicactivado=1
        #se inicia el contador de tiempo
        tiempo1=time.perf_counter()
        #listas para guardar aciertos, errores y estado de la partida
        Lista_aciertos=[]
        Lista_errores=[]
        Lista_partida=[]
        Lista_ahorcado=["_","_","_","_","_","_","_","_"]
        #se elige una palabra secreta del diccionario
        secret=str(random.choice(dic))
        dic.remove(secret)
        palabra=secret
        secret=list(secret)
        #se inicializa la lista de la partida con guiones bajos
        for x in range(len(secret)):
            Lista_partida.append("_")
        #se muestra el estado inicial de la palabra
        print("[ "+ " , ".join(Lista_partida)+ " ]")
        #contador de errores inicializado en -1
        error=-1
    else:
        #se inicia el contador de tiempo
        tiempo1=time.perf_counter()
        #listas para guardar aciertos, errores y estado de la partida
        Lista_aciertos=[]
        Lista_errores=[]
        Lista_partida=[]
        Lista_ahorcado=["_","_","_","_","_","_","_","_"]
        #se elige una palabra secreta aleatoria y se elimina de la lista
        secret=str(random.choice(Lista_palabrasecreta))
        Lista_palabrasecreta.remove(secret)
        palabra=secret
        secret=list(secret)
        #se inicializa la lista de la partida con guiones bajos
        for x in range(len(secret)):
            Lista_partida.append("_")
        #se muestra el estado inicial de la palabra
        print("[ "+ " , ".join(Lista_partida)+ " ]")
        #contador de errores inicializado en -1
        error=-1
    #se comprueba si el usuario tiene multiplicadores disponibles
    if por2 != 0 or por3 != 0 or por4 != 0 or por5 != 0:
        #se pide al usuario si quiere usar un multiplicador
        while mult != 0 and mult != 2 and mult != 3 and mult != 4 and mult != 5:
            mult=input("¿Deseas usar algún multiplicador? (2/3/4/5/0): ")
            while mult not in "23450" or mult.isnumeric() == False:
                print("Respuesta incorrecta.")
                mult=input("¿Deseas usar algún multiplicador? (2/3/4/5/0): ")
            mult=float(mult)
            #se comprueba el tipo de multiplicador y si está disponible
            if mult == 2:
                if por2 == 0:
                    print("No tienes multiplicadores de este tipo.")
                else:
                    mult=2
                    por2-=1
            elif mult == 3:
                if por3 == 0:
                    print("No tienes multiplicadores de este tipo.")
                else:
                    mult=3
                    por3-=1
            elif mult == 4:
                if por4 == 0:
                    print("No tienes multiplicadores de este tipo.")
                else:
                    mult=4
                    por4-=1
            elif mult == 5:
                if por5 == 0:
                    print("No tienes multiplicadores de este tipo.")
                else:
                    mult=5
                    por5-=1
        #si no quiere usar multiplicador
        if mult == 0:
            print("Recibido, sin multiplicadores.")
            mult=1
    else:
        mult=1
    #bucle principal del juego hasta ganar o perder
    while Lista_ahorcado != ["A","H","O","R","C","A","D","O"] and Lista_partida != secret:
        pos=-1
        #si el usuario tiene comodines disponibles
        if com1 != 0 or com2 != 0:
            comusado=float(0)
            como=float(-1)
            #se pregunta si quiere usar un comodín
            while comusado == 0 and como != 0 and Lista_ahorcado[6] == "D" or comusado == 0 and vocaluso != 1 and com2 != 0:
                pos=-1
                como=input("¿Deseas usar un comodín, teniendo en cuenta que no dan puntos? (1/2/0): ")
                while como not in "120" or como.isnumeric() == False:
                    print("Respuesta incorrecta.")
                    como=input("¿Deseas usar un comodín, teniendo en cuenta que no dan puntos? (1/2/0): ")
                como=float(como)
                #comodín 1: revela una letra aleatoria
                if como == 1:
                    if com1 == 0:
                        print("No tienes comodines de este tipo.")
                    else:
                        com1-=1
                        while comusado != 1:
                            pos=random.randint(0,len(secret))-1
                            if Lista_partida[pos] == "_":
                                Lista_partida.pop(pos)
                                Lista_partida.insert(pos,secret[pos])
                                if secret.count(secret[pos]) == Lista_partida.count(secret[pos]):
                                    Lista_aciertos.append(secret[pos])
                                comusado+=1
                            pos=-1
                        print("[ "+ " , ".join(Lista_partida)+ " ]")
                #comodín 2: revela todas las vocales
                elif como == 2:
                    if com2 == 0:
                        print("No tienes comodines de este tipo.")
                    elif vocaluso != 0:
                        print("Ya se ha usado el comodín.")
                    else:
                        com2-=1
                        vocaluso+=1
                        #se recorren las vocales sin tilde
                        for xy in list(sinti):
                            pos=-1
                            for xyz in secret:
                                pos=pos+1
                                if xy == xyz:
                                    Lista_partida.pop(pos)
                                    Lista_partida.insert(pos,secret[pos])
                                    Lista_aciertos.append(secret[pos])
                        #se hace lo mismo con las vocales con tilde
                        for a in list(tilde):
                            pos=-1
                            for b in secret:
                                pos=pos+1
                                if a == b:
                                    Lista_partida.pop(pos)
                                    Lista_partida.insert(pos,secret[pos])
                                    Lista_aciertos.append(secret[pos])
                        print("[ "+ " , ".join(Lista_partida)+ " ]")
            pos=-1
        #si ya se ha completado la palabra se sale del bucle
        if Lista_partida == secret:
            break
        #se pide una letra al usuario
        letra=str(input("Introduce una letra: "))
        #se comprueba que la letra no haya sido usada antes
        while letra.lower() in Lista_errores or letra.upper() in Lista_errores or letra.lower() in Lista_aciertos or letra.upper() in Lista_aciertos:
            print("Esa letra ya la usaste.")
            letra=str(input("Introduce una letra: "))
        #se comprueba que lo introducido sea válido
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
                for y in secret:
                    pos=pos+1
                    #si la letra tiene tilde se convierte
                    if letra.lower() in tilde or letra.upper() in tilde:
                        letra=sinti[tilde.find(letra)]
                    #se hacen las comprobaciones de coincidencia
                    if y == letra:
                        Lista_partida.pop(pos)
                        Lista_partida.insert(pos,y)
                    elif y == letra.lower():
                        Lista_partida.pop(pos)
                        Lista_partida.insert(pos,y)
                    elif y == letra.upper():
                        Lista_partida.pop(pos)
                        Lista_partida.insert(pos,y)
                    #se comprueba también el caso con tilde
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
                        Lista_aciertos.append(letra2)
                print("[ "+ " , ".join(Lista_partida)+ " ]")
                Lista_aciertos.append(letra)
                #se suman puntos por acierto teniendo en cuenta el multiplicador
                puntos+=1*int(mult)
            else:
                #si la letra no está, se suma un error
                error=error+1
                Lista_ahorcado.pop(error)
                Lista_ahorcado.insert(error,["A","H","O","R","C","A","D","O"][error])
                print(*Lista_ahorcado)
                Lista_errores.append(letra)
    #si gana la partida se añaden puntos extra
    if Lista_partida == secret:
        puntos+=10*int(mult)
    #se muestra la palabra secreta
    print("La palabra era",palabra)
    #se calcula el tiempo total
    tiempo2=time.perf_counter()
    print("Aciertos:",len(Lista_aciertos))
    print("Errores:",len(Lista_errores))
    #se calcula el tiempo en minutos y segundos
    stotal=round(tiempo2-tiempo1,0)
    mtotal=0
    while stotal > 60:
        mtotal=mtotal+1
        stotal=stotal-60
    #se guarda la partida en el archivo
    txt=open("Partidas.txt", "a", encoding="utf-8")
    hoy=date.today()
    fecha=hoy.strftime("%d/%m/%Y")
    hora=datetime.now()
    hora=hora.strftime('%H:%M')
    txt.write("Fecha de la partida: "+fecha+"\n")
    txt.write("Hora de la partida: "+hora+"\n")
    txt.write("Palabra secreta: "+palabra+"\n")
    txt.write("Número de aciertos: "+str(len(Lista_aciertos))+"\n")
    txt.write("Número de errores: "+str(len(Lista_errores))+"\n")
    txt.close()
    print(f"Tiempo utilizado: {mtotal} minutos y {int(stotal)} segundos")
    print(f"Tienes {puntos} puntos.")
    #se pregunta si quiere añadir una palabra
    nosi=input("¿Deseas añadir una palabra? (s/n): ")
    while nosi not in "Ss" and nosi not in "Nn" or nosi.isalpha() == False:
        print("Respuesta incorrecta.")
        nosi=input("¿Deseas añadir una palabra? (s/n): ")
    if nosi in "Ss":
        nuevo=input("Introduce la palabra: ")
        while nuevo.isalpha() == False:
            print("Respuesta incorrecta.")
            nuevo=input("Introduce la palabra: ")
        #se añade la palabra dependiendo del modo
        if dicc == "Sí":
            dic.append(nuevo)
            Lista_palabrasecreta.append(nuevo)
        else:
            Lista_palabrasecreta.append(nuevo)
    #se pregunta si quiere abrir la tienda
    nisinino=input("¿Deseas abrir la tienda? (s/n): ")
    while nisinino not in "Ss" and nisinino not in "Nn" or nisinino.isalpha() == False:
        print("Respuesta incorrecta.")
        nisinino=input("¿Deseas abrir la tienda? (s/n): ")
    #sistema de tienda
    if nisinino in "Ss":
        compras="s"
        while compras in "Ss":
            print("Bienvenido a la tienda (1 punto por letra, 10 por palabra)")
            print("1. Comodín letra aleatoria - 5 puntos (aparecerán cuando estés al borde de perder)")
            print("2. Comodín revelar vocales - 10 puntos (están disponibles siempre)")
            print("3. Multiplicador de puntos x2 - 10 puntos")
            print("4. Multiplicador de puntos x3 - 20 puntos")
            print("5. Multiplicador de puntos x4 - 30 puntos")
            print("6. Multiplicador de puntos x5 - 50 puntos")
            print("7. Modo diccionario - 50 puntos")
            print("0. Ver inventario")
            eleccion=input("¿Qué deseas comprar?: ")
            while eleccion not in "01234567" or eleccion.isnumeric() == False:
                print("Respuesta incorrecta.")
                eleccion=input("¿Qué deseas comprar?: ")
            #se gestiona la compra según la opción elegida
            if float(eleccion)==0:
                print("Cerrando tienda.")
            elif float(eleccion)==1:
                if puntos >= 5:
                    com1+=1
                    puntos-=5
                    print("Has adquirido el comodín aleatorio.")
                else:
                    print("No tienes puntos suficientes.")
            elif float(eleccion)==2:
                if puntos >= 10:
                    com2+=1
                    puntos-=10
                    print("Has adquirido el comodín de vocales.")
                else:
                    print("No tienes puntos suficientes.")
            elif float(eleccion)==3:
                if puntos >= 10:
                    por2+=1
                    puntos-=10
                    print("Has adquirido un multiplicador por 2.")
                else:
                    print("No tienes puntos suficientes.")
            elif float(eleccion)==4:
                if puntos >= 20:
                    por3+=1
                    puntos-=20
                    print("Has adquirido un multiplicador por 3.")
                else:
                    print("No tienes puntos suficientes.")
            elif float(eleccion)==5:
                if puntos >= 30:
                    por4+=1
                    puntos-=30
                    print("Has adquirido un multiplicador por 4.")
                else:
                    print("No tienes puntos suficientes.")
            elif float(eleccion)==6:
                if puntos >= 50:
                    por5+=1
                    puntos-=50
                    print("Has adquirido un multiplicador por 5.")
                else:
                    print("No tienes puntos suficientes.")
            elif float(eleccion)==7:
                if puntos >= 50 and dicc == "No":
                    dicc="Sí"
                    puntos-=50
                    print("Has adquirido el modo diccionario.")
                elif dicc == "Sí":
                    print("Ya tienes el modo diccionario.")
                else:
                    print("No tienes puntos suficientes.")
            #se muestra el inventario
            print("Este es tu inventario:")
            print(f"Puntos: {puntos}")
            print(f"Comodín letra aleatoria: {com1}")
            print(f"Comodín revelar vocales: {com2}")
            print(f"Multiplicador x2: {por2}")
            print(f"Multiplicador x3: {por3}")
            print(f"Multiplicador x4: {por4}")
            print(f"Multiplicador x5: {por5}")
            print(f"Modo diccionario: {dicc}")
            #se pregunta si quiere seguir comprando
            if eleccion != 0:
                compras=input("¿Deseas seguir comprando? (s/n): ")
                while compras not in "Ss" and compras not in "Nn" or compras.isalpha() == False:
                    print("Respuesta incorrecta.")
                    compras=input("¿Deseas seguir comprando? (s/n): ")
    #se pregunta si quiere continuar jugando
    sino=input("¿Deseas continuar? (s/n): ")
    while sino not in "Ss" and sino not in "Nn" or sino.isalpha() == False:
        print("Respuesta incorrecta.")
        sino=input("¿Deseas continuar? (s/n): ")