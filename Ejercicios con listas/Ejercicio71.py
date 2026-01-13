#Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.
sino="s"
letras=[]
while sino == "s":
    letra=999
    while str(letra).isalpha() != True:
        letra=str(input("Introduce una letra: "))
        if len(str(letra)) != 1:
            letra=999
    letras.append(str(letra))
    sino=str(input("Deseas repetir (s/n): "))
nodupe=list(set(letras))
print(nodupe)