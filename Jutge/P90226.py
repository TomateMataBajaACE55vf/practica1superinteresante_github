noms=input()
list1=noms.split()
if list1[0] > list1[1]:
    print(list1[0],">",list1[1])
elif list1[0] < list1[1]:
    print(list1[0],"<",list1[1])
elif list1[0] == list1[1]:
    print(list1[0],"=",list1[1])