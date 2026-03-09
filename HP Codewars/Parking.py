coche=int(input())
park=input()
huecos=0
aparcao=1
posletra=int(0)
for i in range(len(park)):
    posletra+=1
    letra=park[i]
    if letra=="_":
        huecos=huecos+1
        if float(huecos)>=float(coche) and aparcao != 0:
            posletra-=coche
            park=list(park)
            for a in range(coche-1):
                park[posletra]="*"
                posletra+=1
            park[posletra]="*"
            aparcao=0
    elif letra=="X":
        huecos=0
if float(aparcao) != 0:
    print(park)
elif float(aparcao) == 0:
    for x in range(len(park)):
        print(park[x], end="")