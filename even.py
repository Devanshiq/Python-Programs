# printing elements on even positions
arr=[]
n=int(input("Enter the number of the elements "))
for i in range(n):
    element=input()
    arr.append(element)
print("The given array is ",arr)
# for i in range(n):
#     if(i%2==0):   # for even positions
#         print("The elements at the even position are ",arr[i]+" ")
#     else:
#         print("The elements at odd positions are ", arr[i]+" ")
#

for i in range(0,n,2):
    print(arr[i])

