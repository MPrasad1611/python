# f(n)=f(n-1)+f(n-2)
n=int(input("enter the number of fib needed:"))
a=0 
b=1
if n==1:
  print(a)
elif n==2:
  print(a,b)
else:
  for i in range(0,n-2):
    c=a+b
    a=b
    b=c
    print(c)