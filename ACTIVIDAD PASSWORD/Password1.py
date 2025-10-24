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
error=str(0)
#se cuenta la longitud del password
passwlen=len(password)
if 6 <= passwlen <= 8:
    pass1=password[0]
    pass2=password[1]
    pass3=password[2]
    pass4=password[3]
    pass5=password[4]
    pass6=password[5]
    if pass1.isnumeric():
        pass1=float(pass1)
        if 1 >= pass1 >=5:
            error=error
        else:
            error="Error en el carácter 1 "
    else:
        error="Error en el carácter 1 "
    if pass2.isalpha():
        pass2=str(pass2)
        if pass2.islower():
            error=error
        else:
            error=error+"Error en el carácter 2 "
    else:
        error=error+"Error en el carácter 2 "
    if pass3.isalpha():
        pass3=str(pass3)
        if pass3.islower():
            error=error
        else:
            error=error+"Error en el carácter 3 "
    else:
        error=error+"Error en el carácter 3 "
    if pass4 in ("*@_"):
        error=error
    else:
        error=error+"Error en el carácter 4 "
    if pass5.isalpha():
        pass5=str(pass5)
        if pass5.islower():
            error=error
        else:
            error=error+"Error en el carácter 5 "
    if pass6.isnumeric():
        pass6=float(pass6)
        if 6 >= pass6 >=9:
            error=error
        else:
            error=error+"Error en el carácter 6 "
    else:
        error=error+"Error en el carácter 6 "
    if passwlen == 7:
        pass7=password[6]
        if pass7 in ("&/#"):
            error=error
        else:
            error=error+"Error en el carácter 7 "
        
        if error == 0:
            print("El formato del PASSWORD es correcto")
            breakpoint
        else:
            print(error)
            breakpoint
    elif passwlen == 8:
        pass7=password[6]
        if pass7 in ("&/#"):
            error=error
        else:
            error=error+"Error en el carácter 7 "
        pass8=password[7]
        if pass8.isnumeric:
            pass8=float(pass8)
            if pass8 >= 5:
                error=error
            else:
                error=error+"Error en el carácter 8"
        else:
            error=error+"Error en el carácter 8"
    else:
        if error == 0:
            print("El formato del PASSWORD es correcto")
            breakpoint
        else:
            print(error)
            breakpoint
else:
    print(f"Error, el password tiene una longitud de {passwlen} caracteres y no cumple los requisitos")