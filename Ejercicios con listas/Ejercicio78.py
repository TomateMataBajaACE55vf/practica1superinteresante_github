#A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
list1=["a","b","D","x","r","X","3","h","w","2","i"]
sino="s"
print("Introduce un valor númerico: ")
while sino in "Ss":
    var=input("Introduce el valor que deseas eliminar: ")
    if var in list1:
        list1.remove(var)
        print(list1)
    else:
        print("El valor introducido no está en la lista.")
    sino=input("Desea introducir otro valor (s/n): ")