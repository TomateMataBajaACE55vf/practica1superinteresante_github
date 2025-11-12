#Imprima el siguiente patrón con el ciclo for. 
for repe in range(5):
    #hacemos que se repita 5 veces
    for pos in range(repe):
        #esta línea hace que se repita repe veces
        print("*",end="")
        #mientras más se repita repe será más grande por lo cual la cantidad de asteriscos será mayor
    print()
    #imprimimos aire para saltar a la siguiente línea y que no se quede en la misma
for repe in range(5,0,-1):
    #hacemos lo mismo al revés
    for pos in range(repe):
        print("*",end="")
    print()