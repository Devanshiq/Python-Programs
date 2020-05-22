# class rectangle():
#     pass
#
#
# r1=rectangle()
# r2=rectangle()
#
#
# r1.height=40
# r1.width=60
#
# r2.height=60
# r2.width=30
#
# print(r1.height*r1.width)
# print(r2.height*r2.width)


# class rectangle():
#     def __init__(self,height,width):
#         print(height*width)
#         self.height=height
#
#         print("The __init__ method is called ")
#
# r1=rectangle(40,60)
# r2=rectangle(50,30)
#
# print(r1.height)
# print(r2.height)


# class rectangle():
#     def __init__(self,*args,**kwargs):
#         self.name="daanshi"
#         self.age=10
# r1=rectangle()

#
# class rectangle():
#     def __init__(self,name):
#         self.a=10
#         self._b=20
#         self.__c=30
#
# r1=rectangle('name')
# print(r1.a)
# print(r1._b)
# print(r1.__c)  #private as double underscores are there


class rectangle():
    def __init__(self,height,width):
        self.__height=height
        self.__width=width

    def set_height(self,value):
        self.__height=value
    def get_height(self):
        return self.__height

    def set_width(self, value):
        self.__width = value

    def get_width(self):
        return self.__width


    def get_area(self):
        return self.__height*self.__width

r1=rectangle(40,30)
r2=rectangle(60,50)

print(r1.get_height())
print("Area of the rectangle r1 is ",r1.get_height()*r1.get_width())
print(r2.get_area())
