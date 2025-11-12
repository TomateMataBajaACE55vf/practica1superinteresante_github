#Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso. Respeta el formato de salida
var1=int(input("Introduce el primer valor: "))
var2=int(input("Introduce el segundo valor: "))
if var1 < var2:
    for num in range(var1,var2):
        print(num,end="-")
    print(var2,end="")
elif var2 < var1:
    for num in range(var1,var2,-1):
        print(num,end="-")
    print(var2,end="")