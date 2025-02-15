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
        print(n)
        break  