arr=[]
n=int(input("Enter the given number of elements "))
for i in range(n):
    inp=input()
    arr.append(inp)
print("The given array is ",arr)
max=arr[0]
for i in range(n):
    if(arr[i]>max):
        max=arr[i]
print("the maximum eleemnt in the array is ",max)