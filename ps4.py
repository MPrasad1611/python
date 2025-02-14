# n=121;
# t=n;
# r=0;
# while n>0:
#     r=r*10+n%10
#     n=n//10
# if t==r:
#     print("Palindrome")
# else:    
#     print("Not Palindrome")

# i=int(input("Choose Operation Number:1.square,2.cube,3.Exit:"))
# while True:
#     if i==1:
#         n=int(input("Enter the number:"))
#         print(n**2)
#         i=int(input("Choose Operation Number:1.square,2.cube,3.Exit:"))
#     elif i==2:
#         n=int(input("Enter the number:"))
#         print(n**3)
#         i=int(input("Choose Operation Number:1.square,2.cube,3.Exit:"))
#     elif i==3:
#         break
#     else:
#         print("Invalid Operation")
#         i=int(input("Choose Operation Number:1.square,2.cube,3.Exit:"))
    
# num=int(input("Enter the number to check if it us a prime:"))
# if  num==1:
#     print("Not Prime")
# elif num==2:
#     print("Prime")
# else: 
#  for i in range(2,num):
#     if num%i==0:
#         print("Not Prime")
#         break
#     else:
#         print("Prime")
#         break
# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))

# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num)
# Swapping two numbers using XOR
a = (input("Enter the first number: "))
b = (input("Enter the second number: "))

print(f"Before swapping: a = {a}, b = {b}")

a = a ^ b
b = a ^ b
a = a ^ b

print(f"After swapping: a = {a}, b = {b}")