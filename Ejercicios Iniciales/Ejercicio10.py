#Introduce por teclado dos números y muestre por pantalla la siguiente información: 
#cociente, resto y si el dividendo es par o impar.
patata1=float(input("Introduce un valor: "))
patata2=float(input("Introduce otro valor: "))

cociente=patata1//patata2
resto=patata1%patata2

print("El cociente es: ",cociente)
print("El resto es: ",resto)

if patata1 % 2 == 0:
    print("El dividendo es par.")
else:
    print("El dividendo es impar")