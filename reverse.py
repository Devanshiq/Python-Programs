# printing the array in reverse order
arr=[]
n=int(input("Enter the numer of elents"))
for i in range(n):
    inp=input()
    arr.append(inp)
print("The given array is ",arr)

# printing the array in reverse order
for i in range(n-1,-1,-1):
    print("the reversearray is ",arr[i])
