# def max(list):
#     max=0;
#     for i in list:
#         if i>max:
#             max=i
#     return max   


# list1=[[7,2,3],[4,2,5],[6,7,8]]
# res=[]
# for j in list1:
#     res.append(max(j))
# print(res)
list1=[1,2,3,4,5,6,7,8,9,10]
key=10
# low=0
# high=len(list1)-1 
# flag=False
# while low<=high:
#       mid=(low+high)//2
#       if list1[mid]==key:
#             flag=True
#             print(f"Element is found at {mid}")
#             break;
#       elif list1[mid]>key:
#             high=mid-1
#       else:
#             low=mid+1
        
# if flag==False:
#     print("Not found")

# def bi(list,key):
#     low=0
#     high=len(list1)-1 
#     while low<=high:
#       mid=(low+high)//2
#       if list1[mid]==key:
#             return mid
#       elif list1[mid]>key:
#             high=mid-1
#       else:
#             low=mid+1
#     return -1
# res=bi(list1,key)
# if res!=-1:
#      print(res)
# else:
#      print("Not Found")
# list1=[1,2,3,4]
# swap=False
# for j in range(len(list1)-1):
#   for i in range(0,len(list1)-j-1):
#     if list1[i]>list1[i+1]:
#        list1[i],list1[i+1]=list1[i+1],list1[i]
#        swap=True
#   if swap==False:
#     print("Alre ady Sorted")
#     break
# print(list1)
