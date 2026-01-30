#Diseñar un programa que al introducir un número calcule la letra correspondiente, teniendo en cuenta los
#siguientes puntos:
#Controlar que"El valor introducido tenga una longitud de 8 dígitos y sea numérico.
#Visualizar"El NIF completo, concatena la letra correspondiente separado con un guion: ej 11111111-R
#Controlar aquellas situaciones en que"El Resto obtenido de un DNI no aparece en la tabla, por tanto, es
#incorrecto. Debe aparecer un mensaje de error.
#Por cada cálculo que se realice,"El programa debe ofrecer la opción de continuar o no, introduciendo
#las letras “s” o “n”. En caso de seleccionar “n” se visualiza MENÚ del apartado 7.
letras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
dnino=[]
dnisi=[]
tries=[]
sino="s"
#Hechas las variables predeterminadas se crea un bucle que define si se repite o no el programa creador de DNIs
while sino in "Ss":
    dni=input("Introduce un DNI: ")
    #Después de introducir el DNI, se observa si tiene una longitud correcta y si son números
    if len(dni) != 8:
        print("El valor introducido tiene una longitud incorrecta.")
        tries.append(0)
        dnino.append(dni)
    elif len(dni) == 8:
        if str(dni).isnumeric() == False:
            print("El valor introducido tiene que ser numérico.")
            tries.append(1)
            dnino.append(dni)
    #Si cumple, se pasa a dividir entre 23 y si el número es mayor que 22 da error, pero sino se guarda el dni con su letra la cual está seleccionada de una lista
    if str(dni).isnumeric():
        divi=float(dni)%23
        if divi > 22:
            print("El valor del DNI es incorrecto.")
            tries.append(2)
            dnino.append(dni)
        else:
            dni=dni+"-"+letras[int(divi)]
            dnisi.append(dni)
            print(dni) 
            tries.append(3)
    sino=input("Deseas introducir otro DNI (s/n): ")
    #Mientras la respuesta no sea SsNn o alfanumérico no acabará el bucle que pregunta
    while sino not in "Ss" and sino not in "Nn" or sino.isalnum() == False:
        print("Respuesta incorrecta.")
        sino=input("Deseas introducir otro DNI (s/n): ")
#Se crean dos variables nosi para saber la opción y final para saber si se finaliza el programa
nosi=0
final=0
while final != 1:
    final=0
    print("RESULTADOS. Escoge una opción:")
    print("1. Listar NIF correcto ordenado de menor a mayor")
    print("2. Listar DNI incorrecto ordenado de menor a mayor")
    print("3. Número total de errores producidos")
    print("4. Número total de DNI correctos")
    print("5. Porcentajes intentos con error y sin error")
    print("6. Salir s/n")
    nosi=input("Introduce una opción: ")
    #Depende del valor indicado se ejecuta una opción
    if nosi.isalnum():
        if nosi in "Ss":
            print("Programa finalizado")
            final=1
        if nosi in "Nn":
            final=2
    if nosi.isnumeric():
        nosi=float(nosi)
    if nosi == 1:
        print(dnisi)
        final=1
    if nosi == 2:
        print(dnino)
        final=1
    if nosi == 3:
        print(len(dnisi))
        final=1
    if nosi == 4:
        print(len(dnino))
        final=1
    if nosi == 5:
        print("El número de intentos es: ",len(tries))
        print("El % de DNI correctos son: ",round(tries.count(3)/len(tries)*100,1))
        print("El % de DNI incorrectos son: ",round(tries.count(0,1,2)/len(tries)*100,1))
        print("El % de DNI con error de longitud es: ",round(tries.count(0)/len(tries)*100,1))
        print("El % de DNI con error de dígitos es: ",round(tries.count(1)/len(tries)*100,1))
        print("El % de DNI que no existen es: ",round(tries.count(2)/len(tries)*100,1))
        final=1
    #Como cada vez que se introduce un valor correcto final cambia a 1 o 2 si sigue siendo 0 resultará en un mensaje de error
    if final == 0:
        print("Respuesta inválida")