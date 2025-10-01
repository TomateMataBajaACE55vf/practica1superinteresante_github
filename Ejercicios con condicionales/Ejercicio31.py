#Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.
word=str(input("Introduce una palabra: "))
ora="A quién madruga Dios ayuda"

if word in ora:
    ind=ora.index(word)
    print("La palabra está en la frase y está en el índice ",ind)
else:
    print("La palabra no está en la frase.")