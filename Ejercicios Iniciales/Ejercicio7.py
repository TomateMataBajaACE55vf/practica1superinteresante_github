#programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes 
#forzar que el resultado de la división tenga 2 decimales?
import math

var1=float(input("Introduce un valor: "))
var2=float(input("Introduce otro valor: "))

total_suma=var1+var2
total_resta=var1-var2
total_multiplicacion=var1*var2
total_division=round(var1/var2,2)
total_potencia=var1**var2
total_raiz1=math.sqrt(var1)
total_raiz2=math.sqrt(var2)
total_division_entera=var1//var2

print("La suma de ",var1," y ",var2," es ",total_suma)
print("La resta de ",var1," y ",var2," es ",total_resta)
print("La multiplicación de ",var1," y ",var2," es ",total_multiplicacion)
print("La división de ",var1," y ",var2," es ",total_division)
print("El exponente de ",var1," y ",var2," es ",total_potencia)
print("La raíz de ",var1," y ",var2," es ",total_raiz1, " y ",total_raiz2, ".")
print("La división entera de ",var1," y ",var2," es ",total_division_entera)
