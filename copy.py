# here we are copying the value of one array into another
arr1=[]
n=int(input("Enter the number of elements"))
for i in range(n):  # range is a number
    inp=input()
    arr1.append((inp))
print("The orirginal array is ",arr1)

# Copying the elements of array1 into array 2
arr2=[None]*len(arr1)     #it is important
for i in range(n):
    arr2[i]=arr1[i]
print("Copied array is ",arr2)