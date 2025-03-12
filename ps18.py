# str1="Welcome to pythons"
# res=""

# for i in str1:
#     if i not in 'aeiou':
#         res=i+res
# print(res)
# words=str1.split()
# max=words[0]
# list1=[]
# for i in words:
#     if len(i)>=len(max):
#         if len(i) > len(max):
#            list1.clear()
#         max=i
#         list1.append(i)
# print(list1)  
# def pali(str1):
#     return str1==str1[::-1]
# str1="abccbc"
# max=str1[0]
# for i in range(len(str1)):
#     for j in range(i+1,len(str1)+1):
#         sub=str1[i:j]
#         if pali(sub):
#             print(sub)
#             if len(sub)>len(max):
#                  max=sub


# print("MAX:",max)    
# str1="takeyouforward"
# pattern="you"
# indexat=-1
# for i in range(len(str1)):
#     flag=True
#     temp=i
#     for j in range(len(pattern)):
#         if temp<len(str1) and str1[temp]==pattern[j]:
#             temp+=1
#         else:
#             flag=False
#             break
#     if flag==True:
#         indexat=i    
# print(indexat)

#patterns
# n=int(input("Enter the no.of stars and rows:"))
# for i in range(0,n):
#     for j in range(0,n):
#         print("* ",end= '')
#     print()
n=int(input("Enter the no.of stars and rows:"))
# for i in range(0,n):
#     for j in range(0,n):
#         if i>=j:
#           print("* ",end= '')
#     print()
# for i in range(0,n):
#     for j in range(0,n):
#         if i<=j:
#           print("* ",end= '')
#         else:
#            print("  ",end='')
#     print()
# for i in range(0,n):
#     for j in range(0,n):
#         if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
#           print("* ",end= '')
#         else:
#            print("  ",end='')
#     print()
# for i in range(0,n):
#     for j in range(0,n):
#         if i==n-1 or j==0  or i==j :
#           print("* ",end= '')
#         else:
#            print("  ",end='')
#     print()
# for i in range(0,n):
#     for j in range(0,n):
#         if i==0 or j==n-1  or i==j :
#           print("* ",end= '')
#         else:
#            print("  ",end='')
#     print()
# for i in range(0,n):
#     for j in range(0,n):
#         if i==0 or j==0 or i+j==n-1:
#           print("* ",end= '')
#         else:
#            print("  ",end='')
#     print()

# for i in range(0,n):
#     for j in range(0,n):
#         if i>=j:
#          print(j+1,end=" ")
#     print()
# count=1
# for i in range(0,n):
#     for j in range(0,n):
#         if i>=j:
#          print(count,end=" ")
#          count+=1
#     print()
for i in range(0,n):
    for j in range(0,n):
        if i>=j:
          print("* ",end= '')
    print()
for i in range(0,n):
    for j in range(0,n):
        if i<=j-1:
          print("* ",end= '')
       
    print()