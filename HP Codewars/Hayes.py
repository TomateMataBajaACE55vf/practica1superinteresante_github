num=input()
max=float(num[0])
for x in range(len(num)):
    if int(num[x]) > int(max):
        max=num[x]
print(int(max))