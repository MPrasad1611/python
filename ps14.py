# list1=[1,2,3,4,5,6,7,8,9,10,344]
# list2=[4,7,9,11,12,34,43,46,67,900]
# low1,low2=0,0
# res=[]
# while low1<len(list1) and low2 < len(list2):
#     if list1[low1]<list2[low2]:
#         res.append(list1[low1])
#         low1+=1
#     else:
#         res.append(list2[low2])
#         low2+=1
    
# res.extend(list1[low1:])
# res.extend(list2[low2:])
# print(res)
def merge(list1,list2):
    low1,low2=0,0
    res=[]
    while low1<len(list1) and low2 < len(list2):
        if list1[low1]<list2[low2]:
            res.append(list1[low1])
            low1+=1
        else:
            res.append(list2[low2])
            low2+=1
    res.extend(list1[low1:])
    res.extend(list2[low2:])
    return res
print(merge([1,2,3,4,5,6,7,8,9,10,344],[4,7,9,11,12,34,43,46,67,900]))