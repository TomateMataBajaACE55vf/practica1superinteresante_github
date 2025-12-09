#Añade al ejercicio anterior la posibilidad de que el programa pregunte si deseas o no continuar introduciendo passwords. Ej. “¿Deseas introducir otro password s/n?
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