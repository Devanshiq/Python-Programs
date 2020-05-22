"""x=100
if x!=100:
    print("value of x is =")
    print(x)
if(x>0):
    print("x is a positive number")
    if(x%2)==0:
        print("it is an even no")
    else:
        print("it is an odd no")

else:
    print("x is a negative number")
print("finish")
name= input("enter a name")
if name=="max":
    print("name enterred is ", name)
elif name=="leo":
    print("name entered is ", name)
else:
    print("invalid name")"""
"""x=[1.2,3,98,"max",[1,2,78]]
print(x)
i=0
while(i<5):
    print("the value of i is",i)
    i=i+1
print("Finished while loop")

num=1
sum=0
print("Enter zero to exit the program")
while num!=0:
    num=float(input("Enter a number "))
    sum=sum+num
    print(sum)
else:
    print("Finished loop")
for x in d.keys():
     print (x)
 for x in d.values():
     print (x)
 for keys,values in d.items():
     print(x)
"""

"""d={"name": "kajal", "age": "20"}
for keys, values in d.items():
    print(keys , values)
for x in range(2,30,3):
    print(x)
else:
    print("Finish")
a={1,2,3,4,9,8,7,5}
for x in a:
    if  (x==4):
        continue
    print(x)
for x in a:
    if (x==7):
        continue
    print(x)"""

"""Function in python"""
"""def sum(args1,args2):
    if type(args1)!=type(args2):
        print("Enter the arguments of same type ")
        return
    return(args1 +args2)

a= sum(14,34)
print(a)
print(sum("hello ","world"))
print(sum("hello",15))
"""

#
# def student(name,age,**marks):
#     print("name ", name)
#     print("age ",age)
#     print("marks ",marks)
#     for key,value in marks.items():
#         print(key,'',value)
# student(12,34,kidjf=890,engkish = 50,science=56)


# class hello():
#     def __init__(self,name):
#         self.a=10
#         self._b=20
#         self.__c=30
#     def public_method(self):
#         print(self.a)
#         print(self.__c)       #accessible inside the class
#         self.__private_method()   #private method can only be called from inside
#     def __private_method(self):
#         print("private ")
# h=hello("mayank")
# print(h.a)
# print(h._b)
# h.public_method()


#
# class parent:
#     def __init__(self,name):
#         print('parent __init__ method  ',name)
# class parent2:
#     def __init__(self,name):
#         print('parent2 __init__ method  ', name)
# class child(parent2,parent):
#     def __init__(self):
#         print("child __init__ method ")
#        # super().__init__("maxxxxx")
#       #  super().__init__("tom")
#        # parent2.__init__(self,"charles")
#         parent.__init__(self,"vaani")
# c1=child()
# print(child.mro())


#PYTHON COMPOSITION
# class salary:
#     def __init__(self,pay,bonus):
#         self.pay=pay
#         self.bonus=bonus
#     def anuual_salary(self):
#         return (self.pay*12)+self.bonus
# class employee:
#     def __init__(self,name,age,pay,bonus):
#         self.name=name                        #similar example can be of book and chapter
#         self.age=age                          #composition represents part of relationship
#         self.obj_salary=salary(pay,bonus)
#     def total_salary(self):
#         return self.obj_salary.anuual_salary()
#
# emp=employee("max",37,15000,10000)
# print(emp.obj_salary.anuual_salary())
# print(emp.total_salary())

#PYTHON AGGREGATION
# class salary:
#     def __init__(self,pay,bonus):
#         self.pay=pay
#         self.bonus=bonus
#     def anuual_salary(self):
#         return (self.pay*12)+self.bonus
# class employee:
#     def __init__(self,name,age):
#         self.name=name                        #similar example can be of book and chapter
#         self.age=age                          #composition represents part of relationship
#         self.obj_salary=salary
#     def total_salary(self):
#         return self.obj_salary.anuual_salary()
#                                                #aggregation represents has a relationship
# salary=salary(15000,10000)                     #salary and emp are independent objects
# emp=employee("max",37)
#
# print(emp.obj_salary.anuual_salary())
# print(emp.total_salary())

def add(x,y=2):
    return x+y
def mul(x,y=3):
    return x*y