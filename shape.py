# class shape:
#     __color=None
#     def set_color(self,color):
#         self.__color=color
#     def get_color(self):
#         return self.__color

# def double(x):
#     return x*2
# def add(x,y):
#     return x+y
# def product(x,y,z):
#     return x*y*z

double=lambda x:x*2
add=lambda x,y:x+y       #lambda is a single line code as we can write above methods in single line code
product=lambda x,y,z:x * y * z

print(double(10))
print(add(10,30))
print(product(10,20,30))

#map,reduce,filter
#their arguments are map(function,iterable collection)  for all of these three
#for using reduce we have to import functools
from functools import reduce  #import reduce function from functools module
list1=[2,3,6,5,8,9,34,12]
list2=[10,11,24,1,6,9]
a=map(lambda x:x*2,list1)
#print(a)
print(list(a))  #cast this to list
#b=map(lambda x,y:x+y,list1)
b= map(lambda x,y:x+y,list1,list2)
print(list(b))

c=filter(lambda x:x%2==0,list1)
print(list(c))
d=filter(lambda x:True if x<=8 else False,list1)
print(list(d))
e= reduce(lambda x,y:x+y,list1)
#print(list(e))
print(e)
f=reduce(lambda x,y:x+y,list2)
print(f)

#Closure functions are able to remember the value which is declared outside the function
#return the closure functions without mentioning parenthesis
