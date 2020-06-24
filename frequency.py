# program to find frequency of each element in array
arr=[]
n = int(input("enter the no of elements"))
for i in range(n):
    inp=input()
    arr.append(inp)
print("the original array is",arr)
fr=[None]*len(arr)
visited=-1
for i in range(n):
    count=1
    for j in range(i+1,n):
        if (arr[i]==arr[j]):
            count+=1
            fr[j]=visited    # that position af array occupies the number -1
    if(fr[i]!=visited):
        fr[i]=count   # give that total count no to a position in frequency array

print("Element frequency ")
for i in range(0,n):
    if(fr[i]!=visited):
        print(" ", arr[i] , " occurs ", fr[i],"times")