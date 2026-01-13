#Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.
words=[]
num=0
#se crean variables y listas vacías
for x in range(int(input("Introduce un número de palabras: "))):
    #se piden los valores correspondientes
    num=num+1
    words.append(str(input(f"Introduce la {num}ª palabra: "))) 
words2=words.copy()
#se duplica la lista y se ordena de diferentes maneras para mostrarse finalmente
words.sort()
words2.sort(reverse=True)
print("lista1 contiene: ",words)
print("lista2 contiene: ",words2)