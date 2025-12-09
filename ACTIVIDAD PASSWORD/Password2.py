#En esta versión, no debes contemplar que se cumplan las condiciones en las posiciones de los índices, pero sí que el total de criterios se cumplan: 3 números (distinguiendo rangos), 3 letras (distinguiendo mayúsculas o minúsculas), 2 símbolos, etc.
bien=int(0)
numdef=int(0)
#He decidido añadir unas condiciones para especificar más en el mensaje final, para mostrar cuantos números hay en cada rango
numbig=int(0)
numsml=int(0)
letdef=int(0)
letbig=int(0)
letsml=int(0)
simdef=int(0)
for pas in range(0,3):
    password=str(input("Introduce un password: "))
    num=int(0)
    let=int(0)
    sim=int(0)
    for pos in range(len(password)):
        if password[pos].isnumeric():
            num=num+1
            numdef=numdef+1
            if float(password[pos]) < 5:
                numsml=numsml+1
            elif float(password[pos]) >= 5:
                numbig=numbig+1
        elif password[pos].isalpha():
            let=let+1
            letdef=letdef+1
            if password[pos].islower:
                letsml=letsml+1
            elif password[pos].isupper:
                letbig=letbig+1
        else:
            sim=sim+1
            simdef=simdef+1
    if num > 2 and let > 2 and sim > 1:
        print("El formato del password es correcto.")
        bien=bien+1
    else:
        print("El formato del password no es correcto.")
print(f"Has introducido {bien} contraseñas válidas.")
print(f"Has introducido {3-bien} contraseñas inválidas.")
print(f"Has introducido {numdef} números de los cuales {numsml} fueron menores que 5 y {numbig} fueron mayores o iguales que 5, {letdef} letras de las cuales {letbig} fueron mayúsculas y {letsml} fueron minúsculas y {simdef} símbolos.")
#Prueba 1: ........, .........., ............ Resultado: Has introducido 0 contraseñas válidas. Has introducido 3 contraseñas inválidas.
#Has introducido 0 números de los cuales 0 fueron menores que 5 y 0 fueron mayores o iguales que 5, 0 letras de las cuales 0 fueron mayúsculas y 0 fueron minúsculas y 30 símbolos.
#Esta prueba sirve mucho para ver huecos en el código y parece ser que ha salido bien.
#Prueba 2: AsDfGhJkLñ, 1234567890, ª!"·$%&/()=?¿ Resultado: 