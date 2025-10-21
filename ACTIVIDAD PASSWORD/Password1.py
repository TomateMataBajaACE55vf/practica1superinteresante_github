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
error=0
#se cuenta la longitud del password
passwlen=len(password)
if 6 <= passwlen <= 8:
    pass1=password[0]
    if pass1.isnumeric():
        pass1=float(password[0])
        if 1 <= pass1 <=5:
            print("KK")
        elif 1 >= password[0] >=5:
            error="Error en el carácter 1""
        elif password[1].islower():
            print("DVAK")
        else:
            error=error+"Error en el carácter 2 "
            print=error
    else:
        error="Error en el carácter 1 "
        if password[1].islower():
            print("DVAK")
            print(error)
        else:
            error=error+"Error en el carácter 2 "
            print=error
else:
    print(f"Error, el password tiene una longitud de {passwlen} caracteres y no cumple los requisitos")