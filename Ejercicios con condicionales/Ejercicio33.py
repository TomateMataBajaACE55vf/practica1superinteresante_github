#Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien año.
frase="No hay mal que dure cien año"
frase=frase.lower()
#Función que permite contar
a=frase.count("a")
e=frase.count("e")
i=frase.count("i")
o=frase.count("o")
u=frase.count("u")
print("El número de a es ",a," el número de e es ",e," el número de i es ",i," el número de o es ",o," y el número de u es ",u)