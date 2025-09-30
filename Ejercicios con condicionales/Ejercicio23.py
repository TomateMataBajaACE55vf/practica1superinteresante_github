#Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
var1=float(input("Introduce un número: "))
if 0 <= var1 <=10:
    if 8.5 < var1 <= 10:
        print("Has sacado un",var1," has sacado un excelente.")
    elif 6.5 <= var1 <= 8.5:
        print("Has sacado un",var1," has sacado un notable.")
    elif 5 <= var1 < 6.5:
        print("Has sacado un",var1," has sacado un satisfactorio.")
    elif 5 > var1:
        print("Has sacado un",var1," has sacado un insuficiente.")
else:
    print("La nota que has introducido no está entre 0 y 10.")