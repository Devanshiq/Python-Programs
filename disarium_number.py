
#disarium number
# 1 + 7*7 + 5*5*5  = 175
# my program is not working here as it is showing 175 is not a disarium number

def calculate_length(number):
    len=0
    while(number!=0):
        len=len+1

        number=number//10          #why the lhs number is treated as comment here
        return len
n = int(input("Enter the input number "))
rem = sum = 0

length=calculate_length(n)
# making a copy of the number
num=n


# calculating the sum of digits powered with their respective positions
while(num>0):
    rem=num % 10
    sum=sum+int(rem**length)
    num=num//10
    length=length-1

#Check whether the sum is equal to the number itself
if(sum==n):
    print(str(n),"is a disarium number")
else:
    print(str(n), "is not a disarium number")
