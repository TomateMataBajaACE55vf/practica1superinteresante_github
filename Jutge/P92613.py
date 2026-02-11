import math
num=float(input())
antes=math.trunc(num)
despues=math.trunc(num+1)
if num == antes:
    despues=num
redondo=round(num)
if num+0.5 == antes+1 and redondo != num+0.5:
    redondo=redondo+1
print(f"{antes} {int(despues)} {redondo}")