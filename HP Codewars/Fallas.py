noches=int(input())
precio=float(input())
total=precio
for x in range(noches-1):
    preciod=precio-precio/10
    total=total+preciod
print(int(total))