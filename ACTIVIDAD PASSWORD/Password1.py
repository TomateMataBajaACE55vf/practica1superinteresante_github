#se muestran las instrucciones del password por pantalla
print("INSTRUCCIONES")
print("1. La longitud del password tiene que tener entre 6 y 8 caracteres")
print("2. Forzar los siguientes valores según la posición indicada:")
print("      Posición 1 Un número mayor o igual que 1 y menor o igual que 5")
print("      Posición 2 Una letra minúscula")
print("      Posición 3 Una letra mayúscula")
print("      Posición 4 Uno de los siguientes símbolos *, _, @")
print("      Posición 5 Una letra minúscula")
print("      Posición 6 Un número mayor o igual que 6 y menor o igual que 9")
print("      Posición 7 Uno de los siguientes símbolos &, /, #")
print("      Posición 8 Un número mayor o igual que 5")
#se pide el password al usuario
password=str(input("Introduce el password: "))
#número de errores es igual a 0 porque no hay 
nume=0
error=""
#se cuenta la longitud del password
passwlen=len(password)
if 6 <= passwlen <= 8:
    #después de ver que cumple con la longitud indicada, se guarda en variables todas las posiciones del password introducido
    pass1=password[0]
    pass2=password[1]
    pass3=password[2]
    pass4=password[3]
    pass5=password[4]
    pass6=password[5]
    #antes de poner la posición 1 como float vemos si es compatible con float
    if pass1.isnumeric():
        pass1=float(pass1)
        if 1 <= pass1 <=5:
            error=error
            #si se cumple, error queda como 0
        else:
            error="Error en el carácter 1 "
            nume=nume+1
    else:
        error="Error en el carácter 1 "
        nume=nume+1
        #si no, se le asigna el mensaje de error y se suma 1 al número de errores
    #comprobamos que sea una letra del alfabeto para luego ver si cumple los requisitos
    if pass2.isalpha():
        pass2=str(pass2)
        if pass2.islower():
            error=error
        else:
            error=error+"Error en el carácter 2 "
            nume=nume+1
    else:
        error=error+"Error en el carácter 2 "
        nume=nume+1
        #Se le suma el mensaje de error
    #se  hace lo mismo con la posición 3
    if pass3.isalpha():
        pass3=str(pass3)
        if pass3.islower():
            error=error
        else:
            error=error+"Error en el carácter 3 "
            nume=nume+1
    else:
        error=error+"Error en el carácter 3 "
        nume=nume+1
    #vemos si el valor de la posición 4 corresponde a alguno de estos símbolos
    if pass4 in ("*@_"):
        error=error
    else:
        error=error+"Error en el carácter 4 "
        nume=nume+1
    #se hace lo mismo que con la posición 3
    if pass5.isalpha():
        pass5=str(pass5)
        if pass5.islower():
            error=error
        else:
            error=error+"Error en el carácter 5 "
            nume=nume+1
    #se hace lo mismo que la posición 1 pero con valores diferentes
    if pass6.isnumeric():
        pass6=float(pass6)
        if 6 >= pass6 >=9:
            error=error
        else:
            error=error+"Error en el carácter 6 "
            nume=nume+1
    else:
        error=error+"Error en el carácter 6 "
        nume=nume+1
    #se ve si el password mide 7 u 8
    if passwlen == 7:
        pass7=password[6]
        #se hace lo mismo que la posición 4 pero con diferentes símbolos
        if pass7 in ("&/#"):
            error=error
        else:
            error=error+"Error en el carácter 7 "
            nume=nume+1
        #si o hay errores se muestra el mensaje y para y si hay muestra los errores y para
        if nume == 0:
            print("El formato del PASSWORD es correcto")
            breakpoint
        else:
            print(error)
            breakpoint
    #se hace lo mismo para si mide 8 pero añadiendo una condición
    elif passwlen == 8:
        pass7=password[6]
        if pass7 in ("&/#"):
            error=error
        else:
            error=error+"Error en el carácter 7 "
            nume=nume+1
        pass8=password[7]
        #se observa si la posición 8 es un número y si es mayor o igual que 5
        if pass8.isnumeric():
            pass8=float(pass8)
            if pass8 >= 5:
                error=error
            else:
                error=error+"Error en el carácter 8"
                nume=nume+1
        else:
            error=error+"Error en el carácter 8"
            nume=nume+1
        #se realiza lo mismo que antes para finalizar
        if nume == 0:
            print("El formato del PASSWORD es correcto")
        else:
            print(error)
    else:
        if nume == 0:
            print("El formato del PASSWORD es correcto")
        else:
            print(error)
#si el password tiene una longitud no válida se muestra un mensaje de error
else:
    print(f"Error, el password tiene una longitud de {passwlen} caracteres y no cumple los requisitos")