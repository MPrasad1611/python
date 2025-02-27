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
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def print_m(list1):
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            if i == 0 or j == 0 or i == len(list1) - 1 or j == len(list1[i]) - 1:
                print(list1[i][j], end=" ")
            else:
                print(" ", end=" ")
        print()

print_m(list1)
     