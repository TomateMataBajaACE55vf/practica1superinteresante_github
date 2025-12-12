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
simsim=int(0)
simsimdef=int(0)
#Finalmente decidí poner una condición para los símbolos que se habían quedado muy simples, por eso la contraseña ha de contener una #
for pas in range(0,3):
    password=str(input("Introduce un password: "))
    num=int(0)
    let=int(0)
    sim=int(0)
    simsim=int(0)
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
            if password[pos] == "#":
                simsim=simsim+1
                sim=sim+1
                simdef=simdef+1
                simsimdef=simsimdef+1
            else:
                sim=sim+1
                simdef=simdef+1
    if num > 2 and let > 2 and sim > 1 and simsim > 0:
        print("El formato del password es correcto.")
        bien=bien+1
    else:
        print("El formato del password no es correcto.")
print(f"Has introducido {bien} contraseñas válidas.")
print(f"Has introducido {3-bien} contraseñas inválidas.")
print(f"Has introducido {numdef} números de los cuales {numsml} fueron menores que 5 y {numbig} fueron mayores o iguales que 5, {letdef} letras de las cuales {letbig} fueron mayúsculas y {letsml} fueron minúsculas y {simdef} símbolos de los cuales {simsimdef} eran #.")
#Prueba 1: ........, .........., ............ Resultado: Has introducido 0 contraseñas válidas. Has introducido 3 contraseñas inválidas.
#Has introducido 0 números de los cuales 0 fueron menores que 5 y 0 fueron mayores o iguales que 5, 0 letras de las cuales 0 fueron mayúsculas y 0 fueron minúsculas y 30 símbolos de los cuales 0 eran #.
#Esta prueba sirve mucho para ver huecos en el código y parece ser que ha salido bien.

#Prueba 2: AsDfGhJkLñ, 1234567890, ª!"·$%&/()=?¿##### Resultado: Has introducido 0 contraseñas válidas. Has introducido 3 contraseñas inválidas.
#Has introducido 10 números de los cuales 5 fueron menores que 5 y 5 fueron mayores o iguales que 5, 11 letras de las cuales 0 fueron mayúsculas y 11 fueron minúsculas y 12 símbolos de los cuales 5 eran #.
#Esta prueba sirve para el recuento de palabras y sobre todo el condicional de si es #.

#Prueba 3: ,, Resultado: Has introducido 0 contraseñas válidas. Has introducido 3 contraseñas inválidas.
#Has introducido 0 números de los cuales 0 fueron menores que 5 y 0 fueron mayores o iguales que 5, 0 letras de las cuales 0 fueron mayúsculas y 0 fueron minúsculas y 0 símbolos de los cuales 0 eran #.
#Esta prueba para asegurarse de que el código no se invente cosas y que funciona con contraseñas de longitud 0.

#Prueba 4: P4p€c0#1, eI20#P3~, 100$#dos Resultado: Has introducido 3 contraseñas válidas. Has introducido 0 contraseñas inválidas.
#Has introducido 9 números de los cuales 9 fueron menores que 5 y 0 fueron mayores o iguales que 5, 9 letras de las cuales 0 fueron mayúsculas y 9 fueron minúsculas y 6 símbolos de los cuales 3 eran #.
#Para comprovar contraseñas válidas.

#Prueba 5: a, j#.4N05C, australopitecus Resultado: Has introducido 1 contraseñas válidas. Has introducido 2 contraseñas inválidas.
#Has introducido 3 números de los cuales 2 fueron menores que 5 y 1 fueron mayores o iguales que 5, 19 letras de las cuales 0 fueron mayúsculas y 19 fueron minúsculas y 2 símbolos de los cuales 1 eran #.
#Para intercalar correctas e incorrectas.

#Prueba 6: ant009:#, o, LOL-#273 Resultado: Has introducido 2 contraseñas válidas. Has introducido 1 contraseñas inválidas.
#Has introducido 6 números de los cuales 4 fueron menores que 5 y 2 fueron mayores o iguales que 5, 7 letras de las cuales 0 fueron mayúsculas y 7 fueron minúsculas y 4 símbolos de los cuales 2 eran #.
#Lo opuesto a lo anterior.

#Prueba 7: aaa111##, bbb222##, ccc333## Resultado: Has introducido 3 contraseñas válidas. Has introducido 0 contraseñas inválidas.
#Has introducido 9 números de los cuales 9 fueron menores que 5 y 0 fueron mayores o iguales que 5, 9 letras de las cuales 0 fueron mayúsculas y 9 fueron minúsculas y 6 símbolos de los cuales 6 eran #.
#Para ver si funciona el primer rango.

#Prueba 8: AAA999##, BBB888##, CCC777## Resultado: Has introducido 3 contraseñas válidas. Has introducido 0 contraseñas inválidas.
#Has introducido 9 números de los cuales 0 fueron menores que 5 y 9 fueron mayores o iguales que 5, 9 letras de las cuales 0 fueron mayúsculas y 9 fueron minúsculas y 6 símbolos de los cuales 6 eran #.
#Para ver si funciona el segundo rango.

#Prueba 9: lsolsdk213#, p03&lY5#, di2jw9. Resultado: Has introducido 1 contraseñas válidas. Has introducido 2 contraseñas inválidas.
#Has introducido 8 números de los cuales 6 fueron menores que 5 y 2 fueron mayores o iguales que 5, 14 letras de las cuales 0 fueron mayúsculas y 14 fueron minúsculas y 2 símbolos de los cuales 2 eran #.
#Algunas pruebas extra para asegurar.

#Prueba 10: si98s#JA-.EW9ijo#ws2.w-aiIOJ9#2Imd+`, 12¡3aB#c, 29·0#dei#wiI#·OJDE#'093 Resultado: Has introducido 3 contraseñas válidas. Has introducido 0 contraseñas inválidas.
#Has introducido 15 números de los cuales 9 fueron menores que 5 y 6 fueron mayores o iguales que 5, 34 letras de las cuales 0 fueron mayúsculas y 34 fueron minúsculas y 18 símbolos de los cuales 8 eran #.
#Esta prueba para juntar contraseñas cortas y largas.