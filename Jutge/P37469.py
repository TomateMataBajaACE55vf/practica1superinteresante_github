secs=input()
mint=0
hora=0
while float(secs)-60 >= 0:
    secs=float(secs)-60
    mint=mint+1
    if mint == 60:
        mint=0
        hora=hora+1
print(f"{hora} {mint} {int(secs)}")