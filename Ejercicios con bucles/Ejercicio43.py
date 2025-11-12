#Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra
word=str(input("Introduce una palabra: "))
for pos in range(0,len(word)):
    #hacemos que se repita tantas veces como letras tiene la palabra
    print(f"En la posición {pos} está la {word[pos]}")