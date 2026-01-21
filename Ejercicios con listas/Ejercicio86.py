#Diseñar un programa que al introducir un número calcule la letra correspondiente, teniendo en cuenta los
#siguientes puntos:
#Controlar que el valor introducido tenga una longitud de 8 dígitos y sea numérico.
#Visualizar el NIF completo, concatena la letra correspondiente separado con un guion: ej 11111111-R
#Controlar aquellas situaciones en que el Resto obtenido de un DNI no aparece en la tabla, por tanto, es
#incorrecto. Debe aparecer un mensaje de error.
#Por cada cálculo que se realice, el programa debe ofrecer la opción de continuar o no, introduciendo
#las letras “s” o “n”. En caso de seleccionar “n” se visualiza MENÚ del apartado 7.
letras["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
dni=input("Introduce un DNI: ")
if len(dni) !=