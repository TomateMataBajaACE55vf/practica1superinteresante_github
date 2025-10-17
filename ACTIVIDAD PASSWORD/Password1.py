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
#se cuenta la longitud del password
passwlong=len(password)
if 6 <= passwlong <= 8:
    print("KK")
else:
    print(f"Error, el password té una longitud de {passwlong} caràcters i no compleix els requisits")