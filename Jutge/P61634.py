años=input()
if int(años)%4==0:
    if años[-1] not in "0" and años[-2] not in "0":
        print("YES")
    else:
        años=años[:-2]
        if int(años)%4==0:
            print("YES")
        else:
            print("NO")
else:
    print("NO")