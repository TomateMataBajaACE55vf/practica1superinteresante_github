nums=input()
list1=nums.split()
if list1[0] == list1[2] and list1[1] == list1[3]:
    print("=",end=" , ")
elif list1[2] <= list1[0] and list1[1] <= list1[3]:
    print("1",end=" , ")
elif list1[0] <= list1[2] and list1[3] <= list1[1]:
    print("2",end=" , ")
else:
    print("?",end=" , ")
list2=[]
list3=[]
list4=[]
list2.append(list1[0])
list2.append(list1[1])
list3.append(list1[2])
list3.append(list1[3])
if list2[0] > list3[0]:
    list4.append(list2[0])
else:
    list4.append(list3[0])
if list2[1] < list3[1]:
    list4.append(list2[1])
else:
    list4.append(list3[1])
if list4[0] > list4[1]:
    print("[",end="")
    print("]")
    quit()
print("[",end="")
print(list4[0],end="")
print(",",end="")
print(list4[1],end="")
print("]")