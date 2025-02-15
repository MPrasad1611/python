# n=int(input("Enter the number:"))
# temp=n;
# c2=n;
# while True:
#     n-=1
#     c=0
#     if n==1:
#         print("Not Prime")
#         break
#     for i in range(1,n+1):
#         if n%i==0:
#             c+=1  
#     if c==2:
#         min_prime=n
#         break  

# while True:
#     temp+=1
#     c=0
#     for i in range(1,temp+1):
#         if temp%i==0:
#             c+=1  
#     if c==2:
#         max_prime=temp
#         break
# if c2-min_prime>max_prime-c2:
#     print(max_prime)
# else:
#     print(min_prime)
# year=int(input("Enter the year:"))
# while True:
#     year+=1
#     if year%4==0 and year%100!=0 or year%400==0:
#         print(year)
#         break
   
# n=int(input("Enter a Number:"))
# sum=0
# for i in range(1,n):
#      if n%i==0:
#         sum+=i
# if n==sum:
#     print("It is a perfect Number")
# else:
#     print("It Is Not a perfect Number")
# n=int(input("Enter a Number:"))
# t=n
# t1=str(n)
# sum=0
# while n>0:
#     x=n%10;
#     sum+=x**len(t1)
#     n=n//10
# if t==sum:
#     print("it is  armstrong")
# else:
#     print("It is not")
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

for n in range(start, end + 1):
    t = n
    t1 = str(n)
    sum = 0

    while n > 0:
        x = n % 10
        sum += x ** len(t1)
        n = n // 10

    if t == sum:
        print(f"{t} is an Armstrong number")
    # else:
    #     print(f"{t} is not an Armstrong number")

