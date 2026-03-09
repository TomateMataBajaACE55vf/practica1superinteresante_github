tipo=input()
hora=input()
list1=hora.split(":")
secs=int(list1[2])
mint=int(list1[1])
hora=int(list1[0])

if tipo == "Metric":
    segundos=secs+(mint*60)+(hora*3600)
    hora=segundos//10000
    segundos=segundos-hora*10000
    mint=segundos//100
    segundos=segundos-mint*100
    
    while secs>=100 or mint >=100 or hora>=10:
        if secs >= 100:
            secs=secs-100
            mint=mint+1
        elif mint >= 100:
            mint=mint-100
            hora=hora+1
        elif hora >= 10:
            hora=hora-10
elif tipo == "Decimal":
    secs=secs*60
    secs=secs//100
    mint=mint*60
    mint=mint//100
    hora=hora*24
    hora=hora//10
    if secs >= 60:
        secs=secs-60
        mint=mint+1
    if mint >= 60:
        mint=mint-60
        hora=hora+1
    if hora >= 24:
        hora=hora-24
if hora<10:
    hora="0"+str(hora)
if mint<10:
    mint="0"+str(mint)
if secs<10:
    secs="0"+str(secs)
print(f"{hora}:{mint}:{secs}")