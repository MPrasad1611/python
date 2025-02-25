list1=[20,15,26,2,98,6]
list2=sorted(list1)

# print(list1)
# print(list2)
re=[]
for i in list1:
    temp=(len(list2)-(list2.index(i)))
    re.append(temp)
print(re)
print(list2)