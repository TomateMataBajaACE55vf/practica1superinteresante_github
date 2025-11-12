#Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario tenga x oportunidades para ver si letra introducida está en esa palabra.
word=str(input("Introduce una palabra secreta: "))
for pos in range(len(word)):
    let=str(input("Introduce una letra: "))
    if let in word:
        print("La letra existe")
    else:
        print("La letra no existe")