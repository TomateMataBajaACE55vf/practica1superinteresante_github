#Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,’
for num in range(0,99,3):
    #colocamos un 3 para que realice saltos de 3 en 3
    print(num,end=",")
print("",end="99")
#para que no termine en coma añadimos una línea a parte para el valor 99