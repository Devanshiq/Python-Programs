import cv2
import numpy as np
# def nothing(x):
#     print(x)
# img= np.zeros((300,512,3),np.uint8)
# cv2.namedWindow('image')
# cv2.createTrackbar('B','image',0,255,nothing)
# cv2.createTrackbar('G','image',0,255,nothing)
# cv2.createTrackbar('R','image',0,255,nothing)
#
# switch='0: OFF\n 1: ON'
# cv2.createTrackbar(switch ,'image',0,1 ,nothing)
#
# while(1):
#
#    cv2.imshow('image',img)
#    k=cv2.waitKey(1)  & 0xFF
#    if k==ord('h'):
#        break
#    b = cv2.getTrackbarPos('B', 'image')
#    g = cv2.getTrackbarPos('G', 'image')
#    r = cv2.getTrackbarPos('R', 'image')
#    s = cv2.getTrackbarPos(switch , 'image')
#    if s==0:
#        img[:]=(0)
#    else:
#        img[:]=[b,g,r]
# cv2.destroyAllWindows()







# def nothing(x):
#     print(x)
#
#
# cv2.namedWindow('image')
# cp=cv2.createTrackbar('CP','image',10,400,nothing)
# switch='gray/color'
# s=cv2.createTrackbar(switch,'image',0,1,nothing)            #code is not running
# k=cv2.waitKey(1)
# while(1):
#     img = cv2.imread('lena.jpg')
#
#     pos=cv2.getTrackbarPos('CP' ,'image')
#     font=cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(img,str(pos),(40,140),font,2,(0,255,255),4)
#     if k==ord('h'):
#         break
#     cv2.getTrackbarPos(switch,'image')
#     if s==0:
#       pass
#     else:
#       img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#       img=cv2.imshow('image', img)
# cv2.destroyAllWindows()







#
# import cv2
# import numpy as np
# def nothing():
#     pass
# #cv2.namedWindow('Tracking')
# while True:
#  frame=cv2.imread('smarties.png')
#  hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#  l_b=np.array([110,50,50])
#  u_b=np.array([130,255,255])
#  #mask=cv2.inRange(frame,lp,up)
#  mask=cv2.inRange(hsv,l_b,u_b)
#  result=cv2.bitwise_and(frame,frame,mask=mask)
#
#  cv2.imshow('you',frame)
#  cv2.imshow('yourrr', mask)
#  cv2.imshow('urr', result)
#  #cv2.imshow('you', mask)
# # cv2.imshow('you', result)
#
#  k=cv2.waitKey(1) & 0xFF
#  if k==ord('h'):
#    break
# cv2.destroyAllWindows()









#
# #BY TRACKING AS IT IS NOT EAST TO DETERMINE THE UP AND LB
# import cv2
# import numpy as np
# def nothing(x):
#     pass
# cap=cv2.VideoCapture(0)
# cv2.namedWindow('tracking')
# cv2.createTrackbar("LH",'tracking',0,255,nothing)
# cv2.createTrackbar("LS",'tracking',0,255,nothing)
# cv2.createTrackbar("LV",'tracking',0,255,nothing)
#
# cv2.createTrackbar("UH",'tracking',255,255,nothing)    #dummy function as it is necessary to give 5 arguments here
# cv2.createTrackbar("US",'tracking',255,255,nothing)
# cv2.createTrackbar("UV",'tracking',255,255,nothing)
# #cv2.createTrackbar("LH",'tracking',0,255,nothing)
# #cv2.createTrackbar("LS",'tracking',0,255,nothing)
# #cv2.createTrackbar("LV",'tracking',0,255,nothing)
#
# # lh=cv2.getTrackbarPos("LH",'tracking')
# # ls=cv2.getTrackbarPos("LS",'tracking')
# # lv=cv2.getTrackbarPos("LV",'tracking')
# #
# # uh=cv2.getTrackbarPos("UH",'tracking')
# # us=cv2.getTrackbarPos("US",'tracking')
# # uv=cv2.getTrackbarPos("UV",'tracking')
# #lh=cv2.getTrackbarPos("LH",'tracking')
# #ls=cv2.getTrackbarPos("LS",'tracking')
# #lv=cv2.getTrackbarPos("LV",'tracking')
#
# # #POSITIONS PAASSED IN ARRAY
# # #ub=np.array([uh,us,uv])
# # lb=np.array([lh,ls,lv])
# # ub=np.array([uh,us,uv])
# while(1):
#     #frame=cv2.imread("smarties.png")
#     #READING FROM VIDEO
#     _,frame=cap.read()
#     hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#
#     lh = cv2.getTrackbarPos("LH", 'tracking')
#     ls = cv2.getTrackbarPos("LS", 'tracking')
#     lv = cv2.getTrackbarPos("LV", 'tracking')
#
#     uh = cv2.getTrackbarPos("UH", 'tracking')
#     us = cv2.getTrackbarPos("US", 'tracking')
#     uv = cv2.getTrackbarPos("UV", 'tracking')
#     # POSITIONS PAASSED IN ARRAY
#     # ub=np.array([uh,us,uv])
#     lb = np.array([lh, ls, lv])
#     ub = np.array([uh, us, uv])
#
#     #mask = cv2.inRange(hsv, lb, ub)
#     mask=cv2.inRange(hsv,lb,ub)
#     result=cv2.bitwise_and(frame,frame,mask=mask)
#     cv2.imshow("tomato",frame)
#     cv2.imshow("mask", mask)
#     cv2.imshow("result", result)
#     k=cv2.waitKey(1)
#     if k== ord('h'):
#         break
# cap.release()
#cv2.destroyAllWindows()








#SIMPLE IMAGE THRESHOLDING
import cv2
import numpy as np
img=cv2.imread('sudoku.png')
# img=cv2.imread('gradient.png')
# _,thi=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# _,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# _,th3=cv2.threshold(img,200,255,cv2.THRESH_BINARY)
# _,th4=cv2.threshold(img,90,255,cv2.THRESH_TRUNC)
# _,th5=cv2.threshold(img,50,255,cv2.THRESH_TOZERO)
# _,th6=cv2.threshold(img,70,255,cv2.THRESH_TOZERO_INV)

#th7=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)         # 11*11-2=120
th8=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)       #code is not runnnig
# cv2.imshow('saare',img)
# cv2.imshow('samne',thi)
# cv2.imshow('samne2',th2)
# cv2.imshow('samne3',th3)
# cv2.imshow('samne4',th4)
# cv2.imshow('samne5',th5)
# cv2.imshow('samne6',th6)
#cv2.imshow('th7',th7)
cv2.imshow('th8',th8)
cv2.waitKey(0)
cv2.destroyAllWindows()


