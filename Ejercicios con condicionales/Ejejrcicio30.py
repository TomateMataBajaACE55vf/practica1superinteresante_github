#Realiza un programa que controle si la longitud de una frase introducida por teclado esigual, menor o mayor de 11 caracteres. Utiliza elif
ora=str(input("Introduce una oración: "))

long=len(ora)

if long < 11:
    print("La frase tiene más de 11 caracteres.")
elif long > 11:
    print("La frase tiene menos de 11 caracteres.")
else:
    print("La frase tiene 11 caracteres.")