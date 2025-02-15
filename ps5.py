n=int(input("Enter the number:"))
while True:
    n-=1
    c=0
    if n==1:
        print("Not Prime")
        break
    for i in range(1,n+1):
        if n%i==0:
            c+=1  
    if c==2:
        min_prime=n
        break  

while True:
    n+=1
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1  
    if c==2:
        max_prime=n
        break
if n-min_prime>max_prime-n:
    print(max_prime)
else:
    print(min_prime)
# year=int(input("Enter the year:"))
# while True:
#     year+=1
#     if year%4==0 and year%100!=0 or year%400==0:
#         print(year)
#         break
   