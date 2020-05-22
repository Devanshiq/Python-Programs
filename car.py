# class car:
#     pass
#
# ford=car()
# honda=car()
# audi=car()
# ford.speed=200
# honda.speed=400
# audi.speed=100
# ford.color='black'
# honda.color='blue'
# audi.colour='maroon'
# print(ford.speed)
# print(audi.colour)
# print(honda.color)


# class car():
#     def __init__(self,speed,color):
#         print(speed)
#         print(color)
#         self.speed=speed
#         self.color=color       # assignment of attribute to self object(deoting current object)
#         print("The __init__ is called")
#
# ford=car(47,"blut")       #creating objects
# honda=car(50,"black")
# audi=car(90,"brown")
#
# print(ford.speed)
# print(audi.color)

#
# class car():
#     def __init__(self,speed,color):
#         self.__speed=speed
#         self.__color=color
#     def set_speed(self,value):
#         self.__speed=value
#     def get_speed(self):
#         return self.__speed
#
#     def set_color(self, value):
#         self.__color = value
#
#     def get_color(self):
#         return self.__color
#
# ford=car(47,"blut")       #creating objects
# honda=car(50,"black")
# audi=car(90,"brown")
#
# ford.__color="magenta"
# #ford.set_speed(500)
# ford.__speed=200
#
# print(ford.get_speed())
# print(ford.get_color())


 #OPERATOR OVERLOADING

import math
class circle:
    def __init__(self,radius):
        self.__radius=radius
    def get_radius(self):
        return self.__radius
    def area(self):
        return math.pi*self.__radius**2
    def __add__(self, circle_object):
        return (self.__radius+circle_object.__radius)
    def __mul__(self, c_obj):
        return (self.__radius*c_obj.__radius)
    def __lt__(self, c_obj):                #less than
        return (self.__radius<c_obj.__radius)
    def __gt__(self, c_obj):                #greater than
        return (self.__radius>c_obj.__radius)
    def __str__(self):
        return "circle area = "+ str(self.area())
c1=circle(3)
c2=circle(2)
#c3=circle()
#print(c1)
#print(c2)
print(c1.get_radius())
print(c2.get_radius())
c3=c1+c2
print(c3)
#print(c3.get_radius())                 # WHY SHOWING ERROR       #for this you have to write return circle(self.radius+circle_object) in the overloaded addition method
c4=c1*c2*c3
print(c4)
print(c1>c2)            #greater than
print(c1<c2)            #less than
print(str(c1))
print(dir(c1))         #to implement the functions