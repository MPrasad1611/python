# list=[1,4,"prasad",90,7.7]
# rev=[]
# for i in list:
#     rev.insert(0,i)

# list=rev
# print(list)
#list1=[1,2,3,4,5,6,7,8,9,9,9,10,9]
# low=0
# high=len(list)-1
# while low<high:
#     list[low],list[high]=list[high],list[low]
#     low+=1
#     high-=1

# print(list)
# dupl=set()
# uni=set()
# for i in list1:
#     if i in uni:
#         dupl.add(i)
#         uni.remove(i)
#     elif i not in dupl:
#         uni.add(i)
    
# print(list(uni))
# print(list(dupl))



# def dupli(num1):
#     cur=[]
#     while num1>0:
#         res=num1%10
#         if res in cur:
#             return True
#         cur.append(res)
#         num1=num1//10
#         cur.append(res)
#     return False
# list1=[898,654,323,666]
# res=[]
# for i in list1:
#     res.append(dupli(i))
# print(res)

def missing(num1):
    rem=[]
    str1=""
    while num1>0:
        re=num1%10
        # if re not in rem:
        rem.append(re)
        num1=num1//10
    for i in range(1,max(rem)):
        if i not in rem:
            str1+=str(i)
    return str1+" missing"

print(missing(34571))