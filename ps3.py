# actual_username = "joe"
# actual_password = "password123"
# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")
# if username_input == actual_username and password_input == actual_password:
#     print("Welcome Joe")
# elif username_input!=actual_username and password_input!=actual_password: 
#     print("Invalid username")
# elif username_input!=actual_username:
#     print("Invalid username")
# else:
#     print("password is wrong")
#     print("Login Failed")

# path=int(input("Enter the path: "))
# if path==1:
#     print("Enter either bear or snake")
#     animal=input("Enter the name of animal: ").lower()
#     if animal=="bear":
#         print("Choose either fight or escape")
#         action=input("Enter the action: ").lower()
#         if action=="fight":
#             print("Won(1) or Lost(0)")
#             result=int(input("Enter the result: ")).lower()
#             if result==1:
#                 print("You can continue")
#             else:
#                 print("You are dead")
#         elif action=="escape":
#             print("You can continue your journey")
#         else:
#             print("Invalid action")
#     else:
#         print("Choose either kill it or cross it")
#         action2=input("Enter the action: ").lower()
#         if action2=="kill":
#             print("Won(1) or Lost(0)")
#             result2=int(input("Enter the result: ")).lower()
#             if result2==1:
#                 print("You can continue")
#             else:
#                 print("You are dead")
#         elif action2=="cross":
#             print("You can continue your journey")
#         else:
#             print("Invalid action")

# else:
#     pass
# for i in range(1,21):
#     print(f"3 X {i} = {3*i}")
# for i in range(0,101,3):
#     print(3,'X',int(i/3),'=',i)
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# number = int(input("Enter a number to calculate its factorial: "))
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# print(f"The factorial of {number} is {factorial(number)}")
n=12345;
r=0;
while n>0:
    r=r*10+n%10
    n=n//10

print(r)
