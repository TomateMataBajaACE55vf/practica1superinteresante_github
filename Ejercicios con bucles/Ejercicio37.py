#Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.
num=int(input("Introduce el número de notas: "))
for x in range(num):
    nota=float(input("Introduce una nota: "))
    if nota >= 5:
        print("Asignatura aprobada.")
    else:
        print("Asignatura suspendida.")