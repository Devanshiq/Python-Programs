import cv2
# cv2.imread('lena.jpg',0)  #0for grey , 1 for colored , -1forunchanged image
# #cv2.imread('lensjdkd',0)   #giving noerror
# # img=cv2.imread('lendjdjhjf',0)
# # print(img)                  #this code is not giving any error printing the value none
# img=cv2.imread('lena.jpg',-1)
# print(img)
# cv2.imshow('image',img)#1st argument any name and then the 2nd argument is variable(it will display image only for a second)
# #cv2.waitKey(0) #closed by you
# #cv2.waitKey(5000)  #for displaying the image for 5 seconds
# k=cv2.waitKey(0) & 0xFF         #key stored in k variable
# if k==27:   #escape key
#  cv2.destroyAllWindows()     #after closing the photo this method is executed
# elif k==ord('s'):  #key u want to press to make a copy of your image in file before destroying it
#  cv2.imwrite('lena_copy.jpg',img)
#  cv2.destroyAllWindows()
#





# cap=cv2.VideoCapture(0) #0for default camera set , -1forgray mode,1for another set of camera, 2 for another set
# fourcc=cv2.VideoWriter_fourcc(*'XVID')       #code has to be passed
# out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) #to save the file we have created this instance (here the 1st argument is name of the file in which video is stored 2nd argument is fourcc instane 3rd argument is 20 frames per second and 4th argument is image's width and height
#
# print(cap.isOpened())
# while(cap.isOpened()):
# #while(True):   #loop forever
#  ret,frame=cap.read()     #ret will store the true or false if the camera is working and frame is storing the pixel
#  if ret==True:
#   print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#   print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#   #WRITING FRAME IN A FILE
#   out.write(frame)    #we are storing pixel before converting it to gray color(video is saved in bgr mode or colored mode)
#
#   #if you want to show the screen grey
#   gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #from blue green red to gray color (now storing in gray variable now you have to pass gray as an argument in imshow method instead of frame
#   #cv2.imshow('frame',frame)
#   cv2.imshow('frame',gray)
#   k=cv2.waitKey(1) & 0xFF
#   if k==ord('f'):
#     break
#  else:
#   break
# cap.release()
# cv2.destroyAllWindows()






# import numpy as np
# #IMAGE WILL ALWAYS BE LOADED IN BGR FORMAT
# img=cv2.imread('lena.jpg',1)
# #to make ur image black using numpy zeroes
# img=np.zeros([512,512,3],np.uint8)   #height,width,3  and datatype
#
# img=cv2.line(img,(0,0),(255,255),(255,0,0),10,)
# img=cv2.arrowedLine(img,(0,255),(255,255),(0,255,0),10)
# img=cv2.rectangle(img,(145,234),(234,348),(0,0,255),10)
# img=cv2.circle(img,(344,44),44,(0,255,255),-1)  #  -1(thickness) for filling the whole space
# font=cv2.FONT_HERSHEY_SIMPLEX
# img=cv2.putText(img,'OPEN CV',(10,500),font,3,(255,255,0),10,cv2.LINE_AA)
# cv2.imshow('image',img)
# #cv2.setMouseCallback('image', click_event)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




#
# #tocahnge the width and height of the frame
# import datetime     #library
# cap=cv2.VideoCapture(0)
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #number associated with this property is 3
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  #here the number is 4
#
# cap.set(3,500)
# cap.set(4,400)
#
# print(cap.get(3))
# print(cap.get(4))
#
# while(True):
#   ret,frame=cap.read()
#   if(ret==True):
#       font=cv2.FONT_HERSHEY_SIMPLEX
#       text='Width: '+str(cap.get(3))+ ' Height : '+str(cap.get(4))
#       d=str(datetime.datetime.now())
#       cv2.putText(frame,d,(10,50),font,1,(0,255,255),1,cv2.LINE_AA)
#       cv2.imshow('fraame',frame)
#       k= cv2.waitKey(1) & 0xFF
#       if k==ord('h') :
#           break
#   else:
#       break
# cap.release()
# cv2.destroyAllWindows()










#
# import numpy as np
# #e=(i for i in dir(cv2) if 'EVENT' in i) #showing error
# #e=[i for i in dir(cv2) if 'EVENT' in i]
# #print(e)
#
# #MOUSE  click CALL BACK FUNCTION
# def mouse_event(event,x,y,flags,param):
#     if event==cv2.EVENT_LBUTTONDBLCLK:
#         print(x,' ',y)
#         font=cv2.FONT_HERSHEY_SIMPLEX
#         strxy=str(x)+' '+str(y)
#         cv2.putText(img,strxy,(x,y),font,1,(0,255,255),2,cv2.LINE_AA)
#         cv2.imshow('image',img)
#     if event==cv2.EVENT_RBUTTONDOWN:
#         # blue=img(x,y,0)
#         # green=img(x,y,1)               #BGR channels  are zero in case of black screen
#         # red=img(x,y,2)
#         blue = img[x, y, 0]
#         green = img[x, y, 1]  # BGR channels are zero in case of black screen
#         red = img[x, y, 2]
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         strBGR = str(blue) + ' ' + str(green)+' '+' '+str(red)
#         cv2.putText(img, strBGR, (x, y), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
#         cv2.imshow('image', img)
#     #points=[]       #it won't draw the line
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img,(x,y),5,(0,0,255),-1)
#         points.append((x,y))
#         if len(points)>=2:
#             cv2.line(img,points[-1],points[-2],(0,255,0),5)
#         cv2.imshow('image',img)
#     if event == cv2.EVENT_RBUTTONDBLCLK:
#         blue = img[x, y, 0]
#         green = img[x, y, 1]  # BGR channels are zero in case of black screen
#         red = img[x, y, 2]
#         #cv2.circle(img,(x,y),5,(0,255,255),-1)
#         #filling color in whole of black screen
#         color=np.zeros((512,512,3),np.uint8)
#         color[:]=[blue,green,red]
#         cv2.imshow('colorrrr',color)
# # to set the image black screen we use numpy zeroes
# #img=np.zeros((512,512,3),np.uint8)
# img=cv2.imread('lena.jpg',1)
# cv2.imshow('image',img)
# points=[]
# cv2.setMouseCallback('image',mouse_event)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

















import numpy as np
img=cv2.imread('messi5.jpg')
img2=cv2.imread('opencv-logo.png')
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
#Copying the ball
ball=img[280:340,330:390]            #top left corner to right most corner
img[273:333,100:160]=ball            #copying the ball to this location
#resize the image in same size
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
#dist=cv2.add(img,img2) #show erroras they are not of same size
dist=cv2.addWeighted(img,0.7,img2,0.3,0)
cv2.imshow('image',dist)
cv2.waitKey(0)
cv2.destroyAllWindows()









