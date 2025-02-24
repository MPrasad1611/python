# list=[1,4,"prasad",90,7.7]
# rev=[]
# for i in list:
#     rev.insert(0,i)

# list=rev
# print(list)
list1=[1,2,3,4,5,6,7,8,9,9,9,10,9]
# low=0
# high=len(list)-1
# while low<high:
#     list[low],list[high]=list[high],list[low]
#     low+=1
#     high-=1

# print(list)
dupl=set()
uni=set()
for i in list1:
    if i in uni:
        dupl.add(i)
        uni.remove(i)
    elif i not in dupl:
        uni.add(i)
    
print(list(uni))
print(list(dupl))