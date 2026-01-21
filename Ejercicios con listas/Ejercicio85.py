#Te piden realizar un programa en que gestionen la media y la mediana de varias de tres asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el programa debe mostrar la media y mediana los todos los alumnos introducidos
from statistics import median
sino="s"
names=[]
ings=[]
casts=[]
cats=[]
while sino in "Ss":
    name=str(input("Introduce estudiante: "))
    names.append(name)
    ing=float(input("Nota de inglés: "))
    cast=float(input("Nota de castellano: "))
    cat=float(input("Nota de catalán: "))
    ings.append(ing)
    casts.append(cast)
    cats.append(cat)
    sino=str(input("Deseas introducir otro alumno (s/n): "))
ings.sort()
cats.sort()
casts.sort()
print("Ingles: ",ings)
print("Castellano: ",casts)
print("Catalán: ",cats)
meding=sum(ings)/len(names)
medcat=sum(cats)/len(names)
medcast=sum(casts)/len(names)
medning=median(ings)
medncat=median(cats)
medncast=median(casts)
print("La media en inglés es: ",round(meding,1))
print("La media en castellano es: ",round(medcast,1))
print("La media en catalán es: ",round(medcat,1))
print("La mediana en inglés es: ",round(medning,1))
print("La mediana en castellano es: ",round(medncast,1))
print("La mediana en catalán es: ",round(medncat,1))