# list1=[[1,2,3],[4,5,6],[7,8,9]]
# def printm(list1):
#     for i in range(len(list1)):
#       for j in range(len(list1[i])):
#           print(list1[i][j],end=" ")
#       print()  
# printm(list1)
# print("-----------")
# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#           if i<=j:
#            list1[i][j],list1[j][i]=list1[j][i],list1[i][j]
# printm(list1)
# def print_m(list1):
#     for i in range(len(list1)):
#        for j in range(len(list1[i])):
#            if i==0 or j==0 or i==len(list1[i])-1 or j==len(list1[i])-1:
#                print(list1[i][j],end=" ")
#            else:
#                print(" ",end=" ")

#        print()
       

# print_m(list1)     
# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# def print_m(list1):
#     for i in range(len(list1)):
#         for j in range(len(list1[i])):
#             if i == 0 or j == 0 or i == len(list1) - 1 or j == len(list1[i]) - 1:
#                 print(list1[i][j], end=" ")
#             else:
#                 print(" ", end=" ")
#         print()

# print_m(list1)
nofc = int(input())  
list1 = list(map(int, input().split()))  # Convert map object to list  

print(list1[1])  # Print the second element (index 1)  

key = int(input())  
mg = int(input())  

k = 0  
low = 0  
high = len(list1) - 1  

while low <= high:  
    mid = (low + high) // 2  
    k += 1  

    if list1[mid] == key:  # Compare with the value at mid, not mid index  
        if k <= mg:  
            print(k)  # Print the number of steps taken  
        else:  
            print("-1")  # Exceeded mg limit  
        break  
    elif list1[mid] < key:  
        low = mid + 1  # Search in the right half  
    else:  
        high = mid - 1  # Search in the left half  
else:  
    print("-1")  # If the key is not found, print "-1"

     