# dict1={'a':"2","b":"1","c":"-1","d":"-2"}
# def sortdict(dict1):
#     temp=list(dict1.items())
#     for i in range(len(temp)):
#       for j in range(len(temp)-i-1):
#         if temp[j][1]>temp[j+1][1]:
#             temp[j],temp[j+1]=temp[j+1],temp[j]
#     dict1=dict(temp)
#     return dict1
# dict2={"A":{"a":"9","b":"2"},"B":{"a":"3","b":"-8"}}
# for i,j in dict2.items():
#     dict2[i]=sortdict(j)

# print(dict2)

def sortdict(str1):
    temp=list(str1)
    for i in range(len(temp)):
      for j in range(len(temp)-i-1):
        if temp[j]>temp[j+1]:
            temp[j],temp[j+1]=temp[j+1],temp[j]
    finalstr=''.join(temp)
    return finalstr 
# print(sortdict("acgb"))


list1=["ate","eat","tea","cat","act","tac",'hit']
res_dict={}
for i in list1:
    temp=sortdict(i)
    if temp in res_dict:
        res_dict[temp].append(i)
    else:
        res_dict[temp]=[i]
    
print(res_dict)