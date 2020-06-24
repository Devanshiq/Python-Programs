
n=int(input("enter the number of pronic numbers you want to show "))   #for example you have to print all 100 pronic numbers
# testing whether a given number is pronic number or not
# pronic numbers are the numbers equal to the conscutive integers of the numbers
def isPronic_number(num):
    flag = False
    for i in range(1,num+1):
        if(i*(i+1)==num):
            flag=True
    return flag

 #displaying the pronic numbers between 1 to 100
print("the pronic numbers between 1 to 100")
for i in range(1,n+1):
    if(isPronic_number(i)):
        print(i," ")