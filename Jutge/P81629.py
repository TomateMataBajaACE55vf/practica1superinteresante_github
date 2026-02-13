dinero=input()
list1=dinero.split()
cent=float(list1[1])
euro=float(list1[0])
cosos=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
opciones=[500,200,100,50,20,10,5,2,1]
centssss=[50,20,10,5,2,1]
while euro > 0:
    for x in range(len(opciones)):
        if euro >= opciones[x]:
            euro=euro-opciones[x]
            cantidad=cosos[x]
            cosos.pop(x)
            cosos.insert(x,cantidad+1)
            break
while cent > 0:
    for x in range(len(centssss)):
        if cent >= centssss[x]:
            cent=cent-centssss[x]
            cantidad=cosos[x+9]
            cosos.pop(x+9)
            cosos.insert(x+9,cantidad+1)
            break
print("Bitllets de 500 euros:",cosos[0])
print("Bitllets de 200 euros:",cosos[1])
print("Bitllets de 100 euros:",cosos[2])
print("Bitllets de 50 euros:",cosos[3])
print("Bitllets de 20 euros:",cosos[4])
print("Bitllets de 10 euros:",cosos[5])
print("Bitllets de 5 euros:",cosos[6])
print("Monedes de 2 euros:",cosos[7])
print("Monedes de 1 euro:",cosos[8])
print("Monedes de 50 centims:",cosos[9])
print("Monedes de 20 centims:",cosos[10])
print("Monedes de 10 centims:",cosos[11])
print("Monedes de 5 centims:",cosos[12])
print("Monedes de 2 centims:",cosos[13])
print("Monedes de 1 centim:",cosos[14])