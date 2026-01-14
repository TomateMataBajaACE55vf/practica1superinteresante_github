#A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista
sino="s"
letras=[]
while sino == "s":
    letra=999
    while str(letra).isalpha() != True:
        letra=str(input("Introduce una letra: "))
        if len(str(letra)) != 1:
            letra=999
    if letra in "áà":
        letra="a"
    if letra in "éè":
        letra="e"
    if letra in "íìï":
        letra="i"
    if letra in "óò":
        letra="o"
    if letra in "úùü":
        letra="u"
    letras.append(str(letra))
    sino=str(input("Deseas repetir (s/n): "))
nodupe=list(set(letras))
print(nodupe)