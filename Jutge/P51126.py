nums=input()
list1=nums.split()
list2={}
list3={}
list2.append(list1[0])
list2.append(list1[1])
list3.append(list1[2])
list3.append(list1[3])
resultado = list1.intersection(list2)
print('[{}]'.format(', '.join(resultado)))