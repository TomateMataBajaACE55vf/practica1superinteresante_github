nums=input()
list1=nums.split()
maxim=list1[0]
for x in list1:
    if float(x)>float(maxim):
        maxim=x
print(maxim)