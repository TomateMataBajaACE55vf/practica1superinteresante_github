nums=input()
suma=0
list1=nums.split()
if len(list1) == 1:
    nums=input()
    list1.append(nums)
for x in list1:
    suma=suma+float(x)
print(int(suma))