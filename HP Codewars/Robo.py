att=input()
att=att.split()
bola=input()
bola=bola.split()
deff=input()
deff=deff.split()
if int(att[0]) >= int(bola[0]) and int(att[0]) >= int(deff[0]):
    print("OFFSIDE")
else:
    print("GOAL")