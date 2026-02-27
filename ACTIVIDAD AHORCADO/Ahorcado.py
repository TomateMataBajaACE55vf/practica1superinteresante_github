#!/usr/bin/python
# coding: latin-1
import random
import time
from datetime import date, datetime
Lista_palabrasecreta=["palabra","zanguango","competitivo","obtuso","itinerario","longaniza","almendra","matadora","Benidorm","miranda"]
sino="s"
tilde="áéíóú"
sinti="aeiou"
while sino in "Ss":
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
            else:
                error=error+1
                Lista_ahorcado.pop(error)
                Lista_ahorcado.insert(error,["A","H","O","R","C","A","D","O"][error])
                print(*Lista_ahorcado)
                Lista_errores.append(letra)
    print("La palabra era",palabra)
    tiempo2=time.perf_counter()
    print("Aciertos:",len(Lista_aciertos))
    print("Errores:",len(Lista_errores))
    stotal=round(tiempo2-tiempo1,0)
    mtotal=0
    while stotal > 60:
        mtotal=mtotal+1
        stotal=stotal-60
    txt=open("Partidas.txt", "w")
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
    nosi=input("Deseas añadir una palabra (s/n): ")
    while nosi not in "Ss" and nosi not in "Nn" or nosi.isalpha() == False:
        print("Respuesta incorrecta.")
        nosi=input("Deseas añadir una palabra (s/n): ")
    sino=input("Deseas continuar (s/n): ")
    while sino not in "Ss" and sino not in "Nn" or sino.isalpha() == False:
        print("Respuesta incorrecta.")
        sino=input("Deseas continuar (s/n): ")
    if nosi in "Ss":
        nuevo=input("Introduce la palabra: ")
        while nuevo.isalpha() == False:
            print("Respuesta incorrecta.")
            nuevo=input("Deseas añadir una palabra (s/n): ")
        Lista_palabrasecreta.append(nuevo)