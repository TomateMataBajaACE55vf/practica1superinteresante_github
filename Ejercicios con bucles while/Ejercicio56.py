#Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la realización de un pedido, si quiere gestionar otro. El establecimiento contempla los siguientes descuentos: Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5% Si el total a pagar es superior a 30 euros, se aplica un descuento del 15% Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla: • El número de pedidos realizados • Total a pagar. • Total con IVA (10%) • Total con el descuento aplicado.
print("MENÚ")
print("1. Bocadillo de calamares- 9 €")
print("2. Bocadillo de chistorra - 4.5 €")
print("3. Bikini de jamón - 2.5 €")
print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5 €")
print("2. Patatas gruesas - 1.75 €")
print("3. Patatas rústicas - 2 €")
print("BEBIDAS")
print("1. Coca cola - 2 €")
print("2. Acuarius - 1.5 €")
print("3. Agua - 1 €")
print("Ejemplo de 2 pedidos")
precio=float(0)
sino="s"
repe=int(0)
while sino.lower()=="s":
    menu=int(input("Introduce un menu: "))
    comp=int(input("Introduce un acompañamiento: "))
    bebe=int(input("Introduce una bebida: "))
    if menu == 1:
        precio=precio+9
    elif menu == 2:
        precio=precio+4.5
    elif menu == 3:
        precio=precio+2.5
    else:
        print("El valor introducido no es válido, no se ha seleccionado ningún menú.")
    if comp == 1:
        precio=precio+1.5
    elif comp == 2:
        precio=precio+1.75
    elif comp == 3:
        precio=precio+2
    else:
        print("El valor introducido no es válido, no se ha seleccionado ningún acompañamiento.")
    if bebe == 1:
        precio=precio+2
    elif bebe == 2:
        precio=precio+1.5
    elif bebe == 3:
        precio=precio+1
    else:
        print("El valor introducido no es válido, no se ha seleccionado ninguna bebida.")
    repe=repe+1
    sino=str(input("Deseas repetir la operación s/n: "))
if precio >= 20 and precio <= 30:
    piva=precio+(precio/100)*10
    pdes=piva-(piva/100)*5
    des=5
elif precio > 30:
    piva=precio+(precio/100)*10
    pdes=piva-(piva/100)*15
    des=15
print("RESUMEN")
print("Número de pedidos: ",repe)
print("Total a pagar: ",round(precio,2))
print("Total con iva: ",round(piva,2))
print(f"Precio total con descuento del {des}%: {round(pdes,2)}")