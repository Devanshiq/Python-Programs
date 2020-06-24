arr=[]
n=int(input("enter the number of elements "))
for i in range(n):
    inp=input()
    arr.append(inp)
print("the given array is ",arr)
n1=int(input("Enter the nuber of elements by which you have to rotate right "))
for i in range(n1):
    last=arr[n-1]
    for j in range(n-1,-1,-1):
        arr[j]=arr[j-1]
    arr[0]=last
print("Aftre doing the right rotation ",arr)