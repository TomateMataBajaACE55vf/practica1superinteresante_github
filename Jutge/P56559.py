nums=input()
list1=nums.split()
list2=[]
list3=[]
list4=[]
list2.append(list1[0])
list2.append(list1[1])
list3.append(list1[2])
list3.append(list1[3])
if float(list2[0]) > float(list3[0]):
    list4.append(list2[0])
else:
    list4.append(list3[0])
if float(list2[1]) < float(list3[1]):
    list4.append(list2[1])
else:
    if float(list3[1]) < 0:
        list4.append(list2[1])
    else:
        list4.append(list3[1])
if float(list4[0]) == float(list2[0]) and float(list4[0]) != float(list3[0]):
    if float(list4[0]) == float(list4[1]):
        print("?")
    else:
        print("1")
elif float(list4[1]) == float(list3[1]) and float(list4[1]) != float(list2[1]):
    if float(list4[0]) == float(list4[1]):
        print("?")
    else:
        print("2")
elif float(list4[1]) != float(list3[1]) and float(list4[1]) == float(list2[1]) and float(list2[1]) <= 0:
    if float(list4[0]) == float(list4[1]):
        print("?")
    else:
        print("2")
elif float(list4[0]) != float(list2[0]) and float(list4[0]) == float(list3[0]) and float(list3[0]) <= 0:
    if float(list4[0]) == float(list4[1]):
        print("?")
    else:
        print("1")
elif list2 == list3:
    print("=")
else:
    print("?")
