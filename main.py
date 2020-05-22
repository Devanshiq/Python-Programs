# from rectangle import rectangle
# from triangle import triangle
# rect=rectangle()
# tri=triangle()
# rect.set_values(30,40)
# tri.set_values(30,40)
# print(rect.area())
# print(tri.area())
#
# rect.set_color("blue")
# tri.set_color('brown')
#
#
# print(rect.get_color())
# print(tri.get_color())

#
# class coffecup:
#     def __init__(self,temperature):
#         self.temperature=temperature
#     def drink_coffee(self):
#         if (self.temperature>85):
#            # print("Coffee is too hot ")
#             raise Exception("Coffee is tooo hot ")
#         elif(self.temperature<65):
#             #print("Coffee is too cold ")
#             #raise Exception
#             raise ValueError
#         else :
#             print("Coffee is ok ")
#
# cup=coffecup(56)
# cup.drink_coffee()

#CREATING CUSTOM EXCEPTION CLASS
# class CoffeeTooHotException(Exception):      #We make custom exception class by inheriting Exception class
#     def __init__(self,message):
#         super().__init__(message)           #calling Exception class method
#
# class CoffeeToocoldException(Exception):      #We make custom exception class by inheriting Exception class
#     def __init__(self,message):
#         super().__init__(message)           #calling Exception class method
#
#
# class coffecup:
#      def __init__(self,temperature):
#          self.temperature=temperature
#      def drink_coffee(self):
#          if (self.temperature>85):
#             # print("Coffee is too hot ")
#              raise  CoffeeTooHotException("Coffee temperature  "+ str(self.temperature))
#          elif(self.temperature<65):
#              #print("Coffee is too cold ")
#              #raise Exception
#              #raise ValueError
#              raise CoffeeToocoldException("coffee temperature "+ str(self.temperature))
#          else :
#              print("Coffee is ok ")
#
# cup=coffecup(56)
# cup.drink_coffee()


def add_no(a,b):
    return a+b
print(__name__)
if __name__=='__main__':
  print(add_no(4,6))