nums=input()
suma=0
list1=nums.split()
while len(list1) != 3:
    nums=input()
    if nums.isnumeric():
        list1.append(nums)
for x in list1:
    suma=suma+float(x)
print(int(suma))