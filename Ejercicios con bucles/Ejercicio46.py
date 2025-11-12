#A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.
word=str(input("Introduce una palabra: "))
voc=""
con=""
word=word.lower()
#convertimos la palabra en minúscula para que no se confunda el código
for pos in range(len(word)):
    if word[pos] in "aeiouáéíóúàèìòùïü":
        voc=voc+word[pos]
    else:
        con=con+word[pos]
print(f"Las vocales de la palabra {word} son: {voc}")
print(f"Las consonantes de la palabra {word} son: {con}")