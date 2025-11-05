#A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10
num=int(input("Introduce el número de notas: "))
for x in range(num):
    nota=float(input("Introduce una nota: "))
    if nota >= 0 or nota <= 10:
        if nota >= 5:
            print("Asignatura aprobada.")
        else:
            print("Asignatura suspendida.")
    else:
        print("Has introducido una nota equivocada.")