list1=[1,45,8.2,-32,-55,90]
max_mem=list1[0]
min=list1[0]
for i in range(0,len(list1)):
    # print(list1[i])
    if list1[i]>max_mem:
        max_mem=list1[i]
    if list1[i]<min:
        min=list1[i]

print(max_mem)   
print(min) 