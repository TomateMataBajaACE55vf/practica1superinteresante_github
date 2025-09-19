#Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor 
#y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
lado=float(input("Introduce un valor: "))
bmenor=float(input("Introduce otro valor: "))
bmayor=float(input("Introduce otro valor: "))
altura=float(input("Introduce otro valor: "))

per=lado*2+bmenor+bmayor
area=(bmayor+bmenor)*altura/2

print("El perímetro del trapecio es: ",per)
print("El área del trapecio es: ",area)