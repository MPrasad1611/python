# list1=["prasad","sai","yaswanth"]
# str1=input("Enter the string: ")

# di={}
# for i in str1:
#     if i in di:
#         di[i]+=1
#     else:
#         di[i]=1
# print(di)

list1=["prasad","sai","yaswanth"]
fr=[]
for st in list1:
  di={}
  for i in st:
      if i in di:
        di[i]+=1
      else:
        di[i]=1
  print(di)
  fr.append({st: di})
print(fr)