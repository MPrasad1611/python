list1=[20,15,26,2,98,6]
list2=sorted(list1)

# print(list1)
# print(list2)
re=[]
for i in list1:
    temp=list2.index(i)+1
    re.append(temp)
print(re)