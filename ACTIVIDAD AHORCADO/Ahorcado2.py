import random
import time
from datetime import date, datetime
Lista_palabrasecreta=["palabra","zanguango","competitivo","obtuso","itinerario","longaniza","almendra","matadora","Benidorm","miranda","polítoton","polimerasa","argón","enriquecer","oposición","llanura","Vetusta","Ununennio","apoteósico","efervescente","ultratumba"]
sino="s"
tilde="áéíóú"
sinti="aeiou"
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
while sino in "Ss":
    mult=float(1)
    vocaluso=float(0)
    if dicc == "Sí":
        dicsino=input("¿Deseas activar el modo diccionario? (s/n): ")
        while dicsino not in "Ss" and dicsino not in "Nn" or dicsino.isalpha() == False:
            print("Respuesta incorrecta.")
            dicsino=input("¿Deseas activar el modo diccionario? (s/n): ")
    if dicsino in "Ss":
        if float(dicactivado) == 0:
            dic=open("Diccionario.txt", "r", encoding="utf-8")
            dic=dic.read().splitlines()
            dicactivado=1
        tiempo1=time.perf_counter()
        Lista_aciertos=[]
        Lista_errores=[]
        Lista_partida=[]
        Lista_ahorcado=["_","_","_","_","_","_","_","_"]
        secret=str(random.choice(dic))
        dic.remove(secret)
        palabra=secret
        secret=list(secret)
        for x in range(len(secret)):
            Lista_partida.append("_")
        print("[ "+ " , ".join(Lista_partida)+ " ]")
        error=-1
    else:
        tiempo1=time.perf_counter()
        Lista_aciertos=[]
        Lista_errores=[]
        Lista_partida=[]
        Lista_ahorcado=["_","_","_","_","_","_","_","_"]
        secret=str(random.choice(Lista_palabrasecreta))
        Lista_palabrasecreta.remove(secret)
        palabra=secret
        secret=list(secret)
        for x in range(len(secret)):
            Lista_partida.append("_")
        print("[ "+ " , ".join(Lista_partida)+ " ]")
        error=-1
    if por2 != 0 or por3 != 0 or por4 != 0 or por5 != 0:
        while mult != 0 and mult != 2 and mult != 3 and mult != 4 and mult != 5:
            mult=input("¿Deseas usar algún multiplicador? (2/3/4/5/0): ")
            while mult not in "23450" or mult.isnumeric() == False:
                print("Respuesta incorrecta.")
                mult=input("¿Deseas usar algún multiplicador? (2/3/4/5/0): ")
            mult=float(mult)
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
        if mult == 0:
            print("Recibido, sin multiplicadores.")
            mult=1
    else:
        mult=1
    while Lista_ahorcado != ["A","H","O","R","C","A","D","O"] and Lista_partida != secret:
        pos=-1
        letra=str(input("Introduce una letra: "))
        while letra.lower() in Lista_errores or letra.upper() in Lista_errores or letra.lower() in Lista_aciertos or letra.upper() in Lista_aciertos:
            print("Esa letra ya la usaste.")
            letra=str(input("Introduce una letra: "))
        while len(letra) != 1 and list(letra) != secret or letra.isalpha() == False:
            print("Lo que has introducido es incorrecto.")
            letra=str(input("Introduce una letra: "))
        if list(letra) == secret:
            Lista_partida=secret
            print("[ "+ " , ".join(Lista_partida)+ " ]")
        else:
            if letra.lower() in tilde or letra.upper() in tilde:
                for z in tilde:
                    pos=pos+1
                    if z == letra:
                        Lista_partida.pop(pos)
                        Lista_partida.insert(pos,sinti[pos])
                    elif z == letra.lower():
                        Lista_partida.pop(pos)
                        Lista_partida.insert(pos,sinti[pos])
                    elif z == letra.upper():
                        Lista_partida.pop(pos)
                        Lista_partida.insert(pos,sinti[pos])
                pos=-1
            if letra.lower() in secret or letra.upper() in secret:
                for y in secret:
                    pos=pos+1
                    if y == letra:
                        Lista_partida.pop(pos)
                        Lista_partida.insert(pos,y)
                    elif y == letra.lower():
                        Lista_partida.pop(pos)
                        Lista_partida.insert(pos,y)
                    elif y == letra.upper():
                        Lista_partida.pop(pos)
                        Lista_partida.insert(pos,y)
                print("[ "+ " , ".join(Lista_partida)+ " ]")
                Lista_aciertos.append(letra)
                puntos+=1*int(mult)
            else:
                error=error+1
                Lista_ahorcado.pop(error)
                Lista_ahorcado.insert(error,["A","H","O","R","C","A","D","O"][error])
                print(*Lista_ahorcado)
        if com1 != 0 or com2 != 0:
            comusado=float(0)
            como=float(-1)
            while comusado == 0 and como != 0 and Lista_ahorcado[6] == "D" or comusado == 0 and vocaluso != 1 and com2 != 0:
                pos=-1
                como=input("¿Deseas usar un comodín? (1/2/0): ")
                while como not in "120" or como.isnumeric() == False:
                    print("Respuesta incorrecta.")
                    como=input("¿Deseas usar un comodín? (1/2/0): ")
                como=float(como)
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
                elif como == 2:
                    if com2 == 0:
                        print("No tienes comodines de este tipo.")
                    elif vocaluso != 0:
                        print("Ya se ha usado el comodín.")
                    else:
                        com2-=1
                        vocaluso+=1
                        for xy in list(sinti):
                            pos=-1
                            for xyz in secret:
                                pos=pos+1
                                if xy == xyz:
                                    Lista_partida.pop(pos)
                                    Lista_partida.insert(pos,secret[pos])
                                    Lista_aciertos.append(secret[pos])
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
    if Lista_partida == secret:
        puntos+=10*int(mult)
    print("La palabra era",palabra)
    tiempo2=time.perf_counter()
    print("Aciertos:",len(Lista_aciertos))
    print("Errores:",len(Lista_errores))
    stotal=round(tiempo2-tiempo1,0)
    mtotal=0
    while stotal > 60:
        mtotal=mtotal+1
        stotal=stotal-60
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
    nosi=input("¿Deseas añadir una palabra? (s/n): ")
    while nosi not in "Ss" and nosi not in "Nn" or nosi.isalpha() == False:
        print("Respuesta incorrecta.")
        nosi=input("¿Deseas añadir una palabra? (s/n): ")
    if nosi in "Ss":
        nuevo=input("Introduce la palabra: ")
        while nuevo.isalpha() == False:
            print("Respuesta incorrecta.")
            nuevo=input("Introduce la palabra: ")
        if dicc == "Sí":
            dic.append(nuevo)
            Lista_palabrasecreta.append(nuevo)
        else:
            Lista_palabrasecreta.append(nuevo)
    nisinino=input("¿Deseas abrir la tienda? (s/n): ")
    while nisinino not in "Ss" and nisinino not in "Nn" or nisinino.isalpha() == False:
        print("Respuesta incorrecta.")
        nisinino=input("¿Deseas abrir la tienda? (s/n): ")
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
            print("Este es tu inventario:")
            print(f"Puntos: {puntos}")
            print(f"Comodín letra aleatoria: {com1}")
            print(f"Comodín revelar vocales: {com2}")
            print(f"Multiplicador x2: {por2}")
            print(f"Multiplicador x3: {por3}")
            print(f"Multiplicador x4: {por4}")
            print(f"Multiplicador x5: {por5}")
            print(f"Modo diccionario: {dicc}")
            if eleccion != 0:
                compras=input("¿Deseas seguir comprando? (s/n): ")
                while compras not in "Ss" and compras not in "Nn" or compras.isalpha() == False:
                    print("Respuesta incorrecta.")
                    compras=input("¿Deseas seguir comprando? (s/n): ")
    sino=input("¿Deseas continuar? (s/n): ")
    while sino not in "Ss" and sino not in "Nn" or sino.isalpha() == False:
        print("Respuesta incorrecta.")
        sino=input("¿Deseas continuar? (s/n): ")