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

i=int(input("Choose Operation Number:1.square,2.cube,3.Exit:"))
while True:
    if i==1:
        n=int(input("Enter the number:"))
        print(n**2)
        i=int(input("Choose Operation Number:1.square,2.cube,3.Exit:"))
    elif i==2:
        n=int(input("Enter the number:"))
        print(n**3)
        i=int(input("Choose Operation Number:1.square,2.cube,3.Exit:"))
    elif i==3:
        break
    else:
        print("Invalid Operation")
        i=int(input("Choose Operation Number:1.square,2.cube,3.Exit:"))
    
    num=int(input("Enter the number to check if it us a prime:"))
    for i in range(2,num):
        if num%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")