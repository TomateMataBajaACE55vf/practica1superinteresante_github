#Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
a=float(input("Introduce el primer valor: "))
b=float(input("Introduce el segundo valor: "))
c=float(input("Introduce el tercer valor: "))
import math
interior=b**2-4*a*c

if interior < 0:
    print("La raíz no puede ser un valor negativo.")
else:
    raiz=math.sqrt(interior)
    x1=(-b+raiz)/2*a
    x2=(-b-raiz)/2*a
    
    print("El valor de x1 es: ",x1)
    print("El valor de x2 es: ",x2)