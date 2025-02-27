# list1=[20,15,26,2,98,6]
# list2=sorted(list1)

# print(list1)
# print(list2)
# re=[]
# for i in list1:
#     temp=(len(list2)-(list2.index(i)))
#     re.append(temp)
# print(re)
# print(list2)
# list=[8,7,1,6,5,9]
# list.sort();
# low=len(list)//2
# high=len(list)-1
# while low<high:
#     list[low],list[high]=list[high],list[low]
#     low+=1
#     high-=1
# print(list) 
list1=[[3,4,5],[6,7,8],[-10,-11,-12]]
# sum=0
# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         if i==0 or i == len(list1)-1:
#             sum+=list1[i][j]
#         else:
#             if j==0 or j==len(list1[i])-1:
#                sum+=list1[i][j]
# print(sum)
# print(len(list1))
sum=0
# sum2=0
# for i in range(len(list1)):
#     sum+=list1[i][i]
#     if list1[i][i]!=list1[i][len(list1)-i-1]:
#         sum2+=list1[i][len(list1)-i-1]

# print(sum+sum2)
for i in range(len(list1)):
    for j in range(len(list1[i])):
          if i==j or i+j==len(list1)-1:
               sum+=list1[i][j]
               if i==j and i+j==len(list1)-1:
                   sum+=list1[i][j]
print(sum)