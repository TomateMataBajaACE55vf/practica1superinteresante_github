import math
# Realiza un programa que pida al usuario dos números racionales (pueden tener decimales) y
#realice las siguientes operaciones con ellos: suma, resta, multiplicación, división, potencia,
#raíz, división entera. Imprime los resultados de cada operación en pantalla.
var1=float(input("introduce un número racional: "))
var2=float(input("introduce otro número racional: "))

total_suma=var1+var2
total_resta=var1-var2
total_multiplicacion=var1*var2
total_division=var1/var2
total_potencia=var1**var2
total_raiz1=math.sqrt(var1)
total_raiz2=math.sqrt(var2)
total_division_entera=var1//var2

print("la suma de tus bonitos números es ",total_suma)
print("la resta de tus bonitos números es ",total_resta)
print("la multiplicación de tus bonitos números es ",total_multiplicacion)
print("la división de tus bonitos números es ",total_division)
print("la potencia de tus bonitos números es ",total_potencia)
print("la raíz de tus bonitos números es ",total_raiz1, " y ",total_raiz2, ".")
print("la división entera de tus bonitos números ",var1," // ",var2," es ",total_division_entera)

#print("la suma de tus bonitos números ",var1," + ",var2," es ",total)
print("Ahora que hemos terminado eso, vamos a ejecutar una cosilla interesante, jeje...")
#CALCULADORA
operacion=input("¿Qué operación quieres hacer? (suma, resta, multiplicación, división, potencia, raíz, división entera): ")
print("Las almendras dominarán el mundo")