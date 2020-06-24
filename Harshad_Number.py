# if a number is divisible by the sum of its digits then it is called as harshad number
n=int(input("Enter the input number "))
rem=sum=0
num=n
while(n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
if(num%sum==0):
    print("The number is a harshad number ")
else:
    print("The number is not  a harshad number ")

