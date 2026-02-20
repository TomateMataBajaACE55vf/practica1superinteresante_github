import random
Lista_palabrasecreta=["palabra","zanguango","competitivo","obtuso","itinerario","longaniza","almendra","matadora","Benidorm","miranda"]
sino="s"
while sino in "Ss":
    aciertos=[]
    errores=[]
    Lista_partida=[]
    Lista_ahorcado=["_","_","_","_","_","_","_","_"]
    secret=str(random.choice(Lista_palabrasecreta))
    Lista_palabrasecreta.remove(secret)
    secret=list(secret)
    for x in range(len(secret)):
        Lista_partida.append("_")
    print("[ "+ " , ".join(Lista_partida)+ " ]")
    error=-1
    while Lista_ahorcado != ["A","H","O","R","C","A","D","O"] and Lista_partida !=secret:
        pos=-1
        letra=str(input("Introduce una letra: "))
        while letra.lower() in errores or letra.upper() in errores or letra.lower() in aciertos or letra.upper() in aciertos:
            print("Esa letra ya la usaste.")
            letra=str(input("Introduce una letra: "))
        if letra.lower() in secret or letra.upper() in secret:
            for y in secret:
                pos=pos+1
                if y == letra:
                    Lista_partida.pop(pos)
                    Lista_partida.insert(pos,y)
                elif y == letra.lower():
                    Lista_partida.pop(pos)
                    Lista_partida.insert(pos,y)
                elif y == letra.lower():
                    Lista_partida.pop(pos)
                    Lista_partida.insert(pos,y)
            print("[ "+ " , ".join(Lista_partida)+ " ]")
            aciertos.append(letra)
        else:
            error=error+1
            Lista_ahorcado.pop(error)
            Lista_ahorcado.insert(error,["A","H","O","R","C","A","D","O"][error])
            print(*Lista_ahorcado)
            errores.append(letra)
    sino=input("Deseas continuar (s/n): ")
    while sino not in "Ss" and sino not in "Nn" or sino.isalpha() == False:
        print("Respuesta incorrecta.")
        sino=input("Deseas continuar (s/n): ")
    nosi=input("Deseas añadir una palabra (s/n): ")
    while nosi not in "Ss" and nosi not in "Nn" or nosi.isalpha() == False:
        print("Respuesta incorrecta.")
        nosi=input("Deseas añadir una palabra (s/n): ")
    if nosi in "Ss":
        nuevo=input("Introduce la palabra: ")
        while nuevo.isalpha() == False:
            print("Respuesta incorrecta.")
            nuevo=input("Deseas añadir una palabra (s/n): ")
        Lista_palabrasecreta.append(nuevo)