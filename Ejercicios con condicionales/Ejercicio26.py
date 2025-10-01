#Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
letra=str(input("Introduce una letra: "))

if (letra.isupper()):
    print("La letra es mayúscula.")
if (letra.islower()):
    print("La letra es minúscula.")