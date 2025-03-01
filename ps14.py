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

def mergesort(list1,low,high):
     if low==high:
         return list1[low:high+1]
     mid=(low+high)//2
     lef=mergesort(list1,low,mid)
     rig=mergesort(list1,mid+1,high)
     res=merge(lef,rig)
     list1[low:high+1]=res
     return res

list1=[44,54,12,3,56,432,7,8,9,10,344]
mergesort(list1,0,len(list1)-1)
print(list1)