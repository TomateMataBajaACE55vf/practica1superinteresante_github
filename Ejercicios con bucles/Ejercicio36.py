#Programa que sume los n primeros números naturales. n Lo introduce el usuario.
num=int(0)
numnum=int(input("Introduce el número de valores: "))
sumnum=int(0)
for x in range(numnum):
    #sumamos 1 a num para que nos de el siguiente número natural
    num=num+1
    sumnum=sumnum+num
print("La suma total de números naturales es: ",sumnum)