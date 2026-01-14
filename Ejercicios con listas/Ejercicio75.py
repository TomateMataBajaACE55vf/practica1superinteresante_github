#Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
#pantalla los siguientes resultados:
#a. Cantidad total de valores
#b. Cantidad de números
#c. Cantidad de letras
#d. Cantidad de mayúsculas
#e. Suma de los valores numéricos
list1=["a","b","D","x","r","X","3","h","w","2","i"]
a=len(list1)
b=0
c=0
d=0
e=0
for pos in list1:
    if pos.isnumeric():
        b=b+1
        e=e+float(pos)
    elif pos.isalpha():
        c=c+1
        if pos.isupper():
            d=d+1
print("Número de valores: ",a)
print("Cantidad de números: ",b)
print("Cantidad de letras: ",c)
print("Cantidad de mayúsculas: ",d)
print("Suma total de números: ",int(e))
    