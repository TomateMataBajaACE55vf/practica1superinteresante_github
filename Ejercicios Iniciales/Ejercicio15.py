#Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
r=float(input("Introduce el radio: "))
h=float(input("Introduce la altura: "))
import math
area=2*math.pi*r*(r+h)
vol=math.pi*r**2*h
area=round(area,2)
vol=round(vol,2)

print("El área de un cilindro es: ",area)
print("El volumen de un cilindro es: ",vol)