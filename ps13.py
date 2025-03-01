# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n*fact(n-1)

# print(fact(5))
# def fin(n):
#     if n==0 or n==1:
#         return n
#     return fin(n-1)+fin(n-2) 
# print(fin(12))
# def sofd(num):
#     if num==0:
#         return 0
#     rem=num%10
#     return rem+sofd(num//10)
# print(sofd(87686))
# def exponent(a,b):
#     if b==0:
#         return 1
#     return a*exponent(a,b-1)
# print(exponent(2,3))
# str=""
# str1="hi i am prasad"
# for i in str1:
#     str=i+str

# print(str)
# def re(str):
#     if len(str)<=0:
#         return ""
#     return str[-1]+re(str[:-1])
# print(re("hello world"))
# def res(str1,len):
#     if len==0: 
#      return ""
#     return str1[len-1]+res(str1,len-1)
    
# print(res("hello",len('hello')))
# def pa(str1):
#     if len(str1) in [0,1]:
#         return True
#     return str1[0]==str1[-1] and pa(str1[1:-1])
# if(pa("malayalam")):
#     print("palindrome")
def ml(list1):
    if len(list1)==1:
        return list1[0]
    fe=list1[0]
    rec_max=ml(list1[1:])
    fm=fe if fe>rec_max else rec_max
    return fm
print(ml([4,9,6,34,31]))