nums=input()
list1=nums.split()
secs=float(list1[2])
mint=float(list1[1])
hora=float(list1[0])
secs=secs+1
if secs >= 60:
    secs=secs-60
    mint=mint+1
    if mint >= 60:
        mint=mint-60
        hora=hora+1
    if hora >= 24:
        hora=hora-24
if hora < 10:
    print("0",end="")
print(int(hora),end=":")
if mint < 10:
    print("0",end="")
print(int(mint),end=":")
if secs < 10:
    print("0",end="")
print(int(secs))