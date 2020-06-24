#entering a matrix from a user thereis another way by importing numpy
matrix1=[]
a=int(input("Enter the number of the rows of matrix 1 "))
b=int(input("Enter the number of columns of matrix 1"))
for i in range(a):
    aur=[]
    for j in range(b):
        j = int(input())   #can't understand this
       # inp=int(input())
        #aur.append(inp)
        aur.append(j)
    print()
    matrix1.append(aur)
print(matrix1)
matrix2=[]
#a=int(input("Enter the number of the rows of matrix 1 "))
#b=int(input("Enter the number of columns of matrix 1"))
print("Enter the elements of the second matrix")
for i in range(a):
    aur=[]
    for j in range(b):
        j = int(input())   #can't understand this
       # inp=int(input())
        #aur.append(inp)
        aur.append(j)
    print()
    matrix2.append(aur)
print(matrix2)
result=[]
for i in range(a):
    c=[]
    for j in range(b):
       inp=int(input())         # enter only zero in making of this result matrix
       c.append(inp)
    result.append(c)
print(result)
# Addition of two matrices
print("enter the elements of the result matrix as of now enter only zero")
# for addition
for i in range(a):
    for j in range(b):
        result[i][j]=matrix1[i][j]+matrix2[i][j]
# here multiplication is not valid here
# for i in range(a):
#     for i in range(b):
#         for k in range(a):
#             result[i][j]=matrix1[i][k]*matrix2[k][j]
print(result)