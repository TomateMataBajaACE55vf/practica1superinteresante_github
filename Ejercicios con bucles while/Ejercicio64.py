#Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos
ok=int(input("Introduce un número: "))
total=0
pos=0
neg=0
imp=0
par=0
while ok != -99:
    total=total+ok
    if ok >= 0:
        pos=pos+1
    else:
        neg=neg+1
    if ok%2 == 0:
        par=par+1
    else:
        imp=imp+1
    ok=int(input("Introduce un número: "))
print("RESUMEN")
print("El número de pares es ",par)
print("El número de impares es ",imp)
print("El número de positivos es ",pos)
print("El número de negativos es ",neg)
print("El total es ",total)