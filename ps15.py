# list1=["prasad","sai","ram"]
# #res={}
# # for i in list1:
# #     res[i]=len(i)
# # print(res)
# list1=[]
# dict1={"a":1,"b":2,"c":3,"e":2}
# dict2={}
# for i,j in dict1.items():
#         if j in dict2:
#             dict2[j].append(i)
#         else:
#             dict2[j]=[i]

# print(dict2)
# max=float('-inf')
# max_key="Dummy"
# for i,j in dict1.items():
#     if j>max:
#         max=j
#         max_key=i

# print(max)
# print(max_key)
str1=input("Enter the string1:")
str2=input("Enter the string2:")
def anagrams(str1,str2):
    if len(str1)!=len(str2):
        return False
    dict1={}
    for i in str1:
        dict1[i]=dict1.get(i,0)+1
    for j in str2:
        if j not in dict1:
            return False
        if dict1[j]!=str2.count(j):
            return False
    return True
print(anagrams(str1,str2))