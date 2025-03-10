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
str1="takeyouforward"
pattern="forward"
for i in range(len(str1)):
    flag=True
    for j in range(len(pattern)):
        if str1[i+j]==pattern[j]:
            pass
        else:
            flag=False
            break
    if flag==True:
        print("Pattern found")    