arr=[]
# program to left rotate the elements of an array
n= int(input("Enter the elements of an array "))
for i in range(n):
    inp=input()
    arr.append(inp)
print("The given array is ",)
print("The given array is ",arr)
for i in range(n):
    print(arr[i])
n1 =int(input("Enter the no of postions you want to left rotate the element"))
#for k in range(n1)
for i in range(n1):  # no of elements we want to left rotate
      first=arr[0]
      for j in range(n-1):
        arr[j]=arr[j+1]
      arr[n-1]=first

print("The new array is ",arr)