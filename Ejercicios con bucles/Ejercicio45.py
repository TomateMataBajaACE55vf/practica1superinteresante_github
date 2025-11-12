#Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes:
word=str(input("Introduce una palabra: "))
voc=""
con=""
for pos in range(len(word)):
    if word[pos] in "aeiouáéíóú":
        voc=voc+word[pos]
    else:
        con=con+word[pos]
print(f"Las vocales de la palabra {word} son: {voc}")
print(f"Las consonantes de la palabra {word} son: {con}")