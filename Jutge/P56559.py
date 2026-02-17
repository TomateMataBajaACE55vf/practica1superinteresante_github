nums=input()
list1=nums.split()
if list1[0] == list1[2] and list1[1] == list1[3]:
    print("=")
elif list1[2] <= list1[0] and list1[1] <= list1[3]:
    print("1")
elif list1[0] <= list1[2] and list1[3] <= list1[1]:
    print("2")
else:
    print("?")