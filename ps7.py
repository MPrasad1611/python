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
list1=[1,43,3]
tup=print(max_min_sum(list1))
if tup:
    print("The maximum number is: ", tup[0])
    print("The minimum number is: ", tup[1])
    print("The sum of all numbers is: ", tup[2])
else:
    print("The list is empty")