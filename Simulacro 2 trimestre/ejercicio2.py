lista=input()
lista=lista.split("-")
buena=[]
mala=[]
no=[]
larga=""
for x in lista:
    for y in range(len(x)):
        if float(len(x)) < 8 or x.isnumeric() or x.isalpha():
            mala.append(x)
        elif x.isalnum() == False:
            no.append(x)
        else:
            buena.append(x)
        if float(len(x)) > float(len(larga)):
            larga=x
mala=list(dict.fromkeys(mala))
buena=list(dict.fromkeys(buena))
no=list(dict.fromkeys(no))
print("Seguras:",buena)
print("Débiles:",mala)
print("Inválidas:",no)
print("La más larga:",larga)