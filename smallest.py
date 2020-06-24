arr=[]
n=int(input("Enter the given number of elements "))
for i in range(n):
    inp=input()
    arr.append(inp)
print("The given array is ",arr)
min=arr[0]
for i in range(n):
    if(arr[i]<min):
        min=arr[i]
print("the maximum eleemnt in the array is ",min)