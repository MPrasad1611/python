# list1=[1,45,8.2,-32,-55,90]
# max_mem=list1[0]
# min=list1[0]
# for i in range(0,len(list1)):
#     # print(list1[i])
#     if list1[i]>max_mem:
#         max_mem=list1[i]
#     if list1[i]<min:
#         min=list1[i]

# print(max_mem)   
# print(min) 

# a=20;
# b=5;
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# def arthe(q,r):
#     print(q+r)
#     print(q-r)
#     print(q*r)
#     print(q/r)
#     print(q%r)
# arthe(a,b)

a1=int(input("Enter the first person age: "))
a2=int(input("Enter the second person age: "))
a3=int(input("Enter the third person age: "))
if a1>a2 and a3>a2:
    print("second person is youngest among all")
elif a2>a1 and a3>a1:   
    print("First Person is youngest among all")
else:
    print("Third person is youngest among all")


