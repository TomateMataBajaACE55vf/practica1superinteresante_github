#Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
var1=float(input("Introduce el diámetro: "))
import math

per=math.pi*var1
per=round(per,1)
area=math.pi*(var1/2)**2
area=round(area,1)

print("El perímetro del círculo es: ",per)
print("El área del círculo es: ",area)