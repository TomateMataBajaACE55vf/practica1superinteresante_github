#Realiza de nuevo el programa de Password (fase 2). El password debe tener las siguientes consideraciones: 
#Debe tener una longitud entre 6 y 8 caracteres. 
#Debe contener como mínimo: 
#2 números mayores o iguales que 1 y menor o igual que 5 
#2 letras minúsculas 
#1 letra mayúscula 
#2 símbolos (*, _, @, &,/,#) 
#1 número mayor o igual que 6 y menor o igual que 5
sino="s"
while sino == "s":
    num1_5=int(0)
    num6_5=int(0)
    letbig=int(0)
    letsml=int(0)
    simdef=int(0)
    password=str(input("Introduce un password: "))
    for pos in range(len(password)):
        if password[pos] in "*_@&/#":
            simdef=simdef+1
        elif password[pos].isnumeric():
            if int(password[pos]) >= 1 and int(password[pos]) <= 5:
                num1_5=num1_5+1
            if int(password[pos]) <= 5 or int(password[pos]) >= 6:
                num6_5=num6_5+1
        elif password[pos].isalpha():
            if password[pos].islower():
                letsml=letsml+1
            elif password[pos].isupper():
                letbig=letbig+1
    if num1_5 > 1 and num6_5 > 0 and simdef > 1 and letbig > 0 and letsml > 1:
        print("password correcto")
    else:
        print("password incorrecto")
    sino=str(input("¿Deseas introducir otro password (s/n): "))