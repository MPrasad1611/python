# def fact(n):
#     if n==1:
#        return 1
#     temp=fact(n-1)
#     print(temp)
#     return n*temp
# fact(5)
def add(a,b):
    if b==1:
        return a
    return a+add(a,b-1)
print(add(4,3))