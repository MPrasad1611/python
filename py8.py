# list1=["prasad","sai","yaswanth"]
# str1=input("Enter the string: ")

# di={}
# for i in str1:
#     if i in di:
#         di[i]+=1
#     else:
#         di[i]=1
# print(di)

# list1=["prasad","sai","yaswanth"]
# fr=[]
# for st in list1:
#   di={}
#   for i in st:
#       if i in di:
#         di[i]+=1
#       else:
#         di[i]=1
#   fr.append({st: di})
# print(fr)
def max_min_sum(list_p):
    if len(list_p) == 0:
        return
    max = min = list_p[0]
    sum=0
    for i in list_p:
        max=i if i > max else max
        min=i if i < min else min
        sum+=i
    return max, min, sum
list1=[100,2,3,4,5,6,7,8,9,10]
max,min,sum=max_min_sum(list1)
sl=float("-inf")
for i in list1:
    if i!=max and i>sl:
        sl=i
print(sl)