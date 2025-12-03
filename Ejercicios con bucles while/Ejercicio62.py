#Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
uno=int(input("Introduce el inicio: "))
dos=int(input("Introduce el final: "))
par=""
imp=""
if uno > dos:
    for x in range(dos,uno):
        #si el residuo de dividir entre dos es cero se sabe que es par y sino impar
        if x%2 == 0:
            par=par+str(x)+"-"
        if x%2 != 0:
            imp=imp+str(x)+"-"
    print(par[:-1])
    print(imp[:-1])
if dos > uno:
    for x in range(uno,dos):
        if x%2 == 0:
            par=par+str(x)+"-"
        if x%2 != 0:
            imp=imp+str(x)+"-"
    print("Los números pares son ",par[:-1])
    print("Los números impares son ",imp[:-1])