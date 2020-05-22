# class polygon:
#     __height=None
#     __width=None
#     def set_values(self,height,width):
#         self.__height=height
#         self.__width=width
#     def get_height(self):
#         return self.__height
#     def get_width(self):
#         return self.__width
# class rectangle(polygon):
#     def area(self):
#         #return self.__height*self.__width
#          return self.get_height()*self.get_width()
# class triangle(polygon):
#     def area(self):
#        # return self.__height*self.__width/2
#        return self.get_height() * self.get_width()/2

# rect=rectangle()
# tri=triangle()
# rect.set_values(20,40)
# tri.set_values(20,40)
# print(rect.area())
# print(tri.area())



#
# class polygon:
#     __height=None
#     __width=None
#     def set_values(self,height,width):
#          self.__height=height
#          self.__width=width
#     def get_height(self):
#          return self.__height
#     def get_width(self):
#          return self.__width



# class shape():
#      def area(self,side):
#          self.side=side
#          return self.side*self.side
#
#      def perimeter(self,side):
#          self.side=side
#          return 4*self.side
#
#
# class square(shape):
#      def __init__(self):
#          pass
# sq=square()
# print(sq.area(5))
# print(sq.perimeter(3))

# class shape:
#     def __init__(self,side):
#         self.side=side
#
# class square(shape):
#     def area(self):
#         return self.side*self.side
#     def parameter(self):
#         return 4*self.side
#
# sur=square(5)
# print(sur.area())
# print(sur.parameter())

#ABSTRACT CLASSES
# from abc import ABC,abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self): pass
#     @abstractmethod
#     def perimeter(self): pass
#
# class square(shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#             return self.side*self.side
#     def perimeter(self):
#             return 4*self.side


#sq=square(6)
#print(sq.area())
#print(sq.perimeter())


#
# result= None
# a=float(input('Number 1: '))
# b=float(input('Number 2: '))
# try:
#     result =a / b
# except Exception as e:
#     print("Error ",e)
# print("result",result)
# print('end')


# 41st video EXCEPTION HANDLING
result=None
a=float(input("Enter ur first number "))
b=float(input("Enter ur second number "))
try:
    result=a/b
except ZeroDivisionError as e :
    print("Zerodivisionerror ",type(e))
except TypeError as e :
    print("Typeerror " ,type(e))
else:                                        # else statements can not be executed without except statement
    print("else")                            #but finally will always execute
finally:
    print("finally ")

print("result ",result)
print("end")


