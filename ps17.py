# str1="a+b-(d*b-{e/f})"
# strop=""
# for i in str1:
#     if i=="(" or i==")"or i=="{" or i=="}" or i=="[" or i=="]":
#         strop+=""
#     else:
#         strop+=i

# print(strop)

# str1="mom"
# rev=''
# for i in str1:
#     rev+=i

# if rev==str1:
#     print("palindrome")
# else:
#     print("not palindrome")

str1="MALAYALAM"
# low=0
# high=len(str1)-1
# flag=1
# while low<high:
#     if str1[low]==str1[high]:
#         low+=1
#         high-=1
#     else:
#         print("not palindrome")
#         flag=0
#         break
# if low>=high:
#     print("palindrome")
# if flag==1:
#     print("palindrome")
# def pal(str1):
#     low=0
#     high=len(str1)-1
#     while low<high:
#         if str1[low]==str1[high]:
#             low+=1
#             high-=1
#         else:
#             return False
#     return True
# if pal(str1):
#     print("palindrome")
# else:
#     print("not palindrome")
str1="take u bsckward to memories"
dict1={}
for i in str1:
  if i in 'aeiou':  
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
for key,value in dict1.items():
    if value>1:
        print(f"{key} is present {value} times")