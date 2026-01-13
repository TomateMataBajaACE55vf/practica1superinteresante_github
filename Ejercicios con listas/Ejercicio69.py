#Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor.
nums=[]
#después de crear un lista vacía se piden los números
for x in range(int(input("Introduce un número de valores: "))):
    nums.append(int(input("Introduce un número: "))) 
#al final se ordenan y se muestran
nums.sort()
print(nums)