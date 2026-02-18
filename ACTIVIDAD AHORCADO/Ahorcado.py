import random
Lista_palabrasecreta=["palabra","zanguango","competitivo","obtuso","itinerario","longaniza","almendra","matadora","Benidorm","maravilloso"]
Lista_partida=[]
Lista_ahorcado=["_","_","_","_","_","_","_","_"]
Lista_palabrasecreta=str(random.choice(Lista_palabrasecreta))
Lista_palabrasecreta=list(Lista_palabrasecreta)
for x in range(len(Lista_palabrasecreta)):
    Lista_partida.append("_")
print("[ "+ " , ".join(Lista_partida)+ " ]")
errores=-1
while Lista_ahorcado != ["A","H","O","R","C","A","D","O"]:
    pos=-1
    letra=str(input("Introduce una letra: "))
    if letra in Lista_palabrasecreta:
        for y in Lista_palabrasecreta:
            pos=pos+1
            if y == letra:
                Lista_partida.remove(pos)
                Lista_partida.insert(pos,letra)
        print("[ "+ " , ".join(Lista_partida)+ " ]")
    else:
        errores=errores+1
        Lista_ahorcado.remove(errores)
        Lista_ahorcado.insert(errores,["A","H","O","R","C","A","D","O"][errores])