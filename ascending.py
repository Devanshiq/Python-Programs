# not working when the no of digits are different when you don;t mention int while taking the input

arr=[]
temp=0
n=int(input("enter the number of elements "))
for i in range(0,n):
    inp=int(input())
    arr.append(inp)
print("The given array is ",arr)

for i in range(0,n):
    for j in range(i+1,n):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("After sorting the array is ",arr)
for i in range(n):
    print(arr[i]," ")
print("now printing the eelments in descending order")
arr.sort(reverse=True)
print(arr)