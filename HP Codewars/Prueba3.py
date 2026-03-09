import random
numsec=float(random.randint(1,100))
inputo=float(input())
tries=float(0)
while inputo != numsec:
    if inputo < numsec:
        print("Lower")
    elif inputo > numsec:
        print("Higher")
    tries+=1
    inputo=float(input())
if tries < 50:
    print("Correct")
else:
    print("Failed to find the number in 50 attempts.")