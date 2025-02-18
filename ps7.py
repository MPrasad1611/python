# def max_min_sum(list_p):
#     if len(list_p) == 0:
#         return
#     max = min = list_p[0]
#     sum=0
#     for i in list_p:
#         max=i if i > max else max
#         min=i if i < min else min
#         sum+=i
#     return max, min, sum
# list1=[1,43,3]
# tup=print(max_min_sum(list1))
# if tup:
#     print("The maximum number is: ", tup[0])
#     print("The minimum number is: ", tup[1])
#     print("The sum of all numbers is: ", tup[2])
# else:
#     print("The list is empty")

def find_element(list1,x):
    if len(list1) == 0:
        return
    for i in list1:
        if i== x:
            return list1.index(i)
    return -1

list1=[1,2,34,22,43,27]
x=22
x1=find_element(list1,x)
if x1 != -1:
    print("element found at index",x1)
else:
    print("element not found")
# if find_element(list1,x):
#     print("element found")
# else:
#     print("element not found")