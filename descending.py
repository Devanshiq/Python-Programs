# arr=[1,24,456,44,435,23,477,788,13]
arr=[]
n=int(input("enter the number of elements "))
for i in range(n):
    inp=int(input())
    arr.append(inp)
print("The given array is ",arr)
temp=0
for i in range(n):
    for j in range(i+1,n):
        if(arr[i]< arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
#print("After sorting the array is ",arr)
for i in range(n):
    print(arr[i]," ")
print("now printing the eelments in ascending order")
arr.sort()
print(arr)