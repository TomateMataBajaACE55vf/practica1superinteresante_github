#Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas.
word=str(input("Introduce una palabra: "))
ora="A quién madruga Dios ayuda"
ora=ora.lower()
mayus=word.upper()
minus=word.lower()

if mayus in ora:
    ind=ora.index(mayus)
    print("La palabra está en la frase y está en el índice ",ind)
elif minus in ora:
    ind=ora.index(minus)
    print("La palabra está en la frase y está en el índice ",ind)
else:
    print("La palabra no está en la frase.")