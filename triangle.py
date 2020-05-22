# from polygon import polygon
# from shape import shape
# class triangle(polygon,shape):                      #Multiple Inheritance
#    def area(self):
#         # return self.__height*self.__width/2
#         return self.get_height() * self.get_width()/2


# result = None
# a = float(input("Enter ur first number "))
# b = float(input("Enter ur second number "))
# try:
#   result = a / b
# finally:
#  print("finally ")
#
# print("result ", result)
# print("end")

# import  main
# print(main.add_no(7,8))
#

import _thread
import time              #we can import time module as thread module is already imported
def print_epoch(nameofthread,delay):                   #name of the function   print_epoch
    count=0
    while count<4:
        time.sleep(delay)
        count=count+1
        print(nameofthread,"-------------------",time.time())
try:
   _thread.start_new_thread(print_epoch,("thread 1",1))                 #ist argument is name of the function , 2nd argument is a tuple consisting
   _thread.start_new_thread(print_epoch,("thread 2",3))                 #of the arguments that we have passed in our main function and the 3rd argument is the optional one for entering dictionary(key-value pair)
except:
   print("name of the error")

#input()                 #function for waiting
while 1:                 #forever loop also a function for waiting
    pass       #in order to avoid unhandled exception we have to apply try catch block