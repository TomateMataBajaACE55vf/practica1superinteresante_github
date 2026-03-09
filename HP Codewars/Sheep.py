hola=input()
hola=hola.split()
todo=float(0)
for y in hola:
    todo=todo+float(y)
max=hola[0]
min=hola[0]
for x in range(len(hola)):
    if int(hola[x]) > int(max):
        max=hola[x]
    elif int(hola[x]) < int(min):
        min=hola[x]
inicio=float(min)
toda=0
while inicio <= float(max):
    toda=toda+inicio
    inicio+=1
print(int(toda-todo))