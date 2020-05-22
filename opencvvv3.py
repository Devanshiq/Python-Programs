# # import cv2
# # from matplotlib import pyplot as plt
# # img=cv2.imread('lena.jpg',)
# # cv2.imshow('image',img)            #in this image is dipalyed in bgr channels but in matplotlib it is dispalyed in rgb channel so converting image to rgb channel
# # img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# # plt.imshow(img)
# # plt.xticks([])            #to hide the scaling
# # plt.yticks([])
# # plt.show()
# # cv2.waitKey(0)
# #cv2.destroyAllWindows()
#
#
#
#
#
# #
# # import cv2
# # import numpy as np
# # from matplotlib import pyplot as plt
# # img=cv2.imread('gradient.png')
# # _,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# # _,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# # #_,th3=cv2.threshold(img,200,255,cv2.THRESH_BINARY)
# # _,th4=cv2.threshold(img,90,255,cv2.THRESH_TRUNC)
# # _,th5=cv2.threshold(img,50,255,cv2.THRESH_TOZERO)
# # _,th6=cv2.threshold(img,70,255,cv2.THRESH_TOZERO_INV)
# #
# # #DISPLAYING ALL THREE OF THEM IN SINGLE LINE
# # titles=['Original image','THRESH_BINARY','THRESH_BINARY_INV','THRESH_TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV']
# # images=[img,th1,th2,th4,th5,th6]
# # for i in range(6):
# #     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
# #     plt.xticks([]),plt.yticks([])
# #     plt.title([titles[i]])
# # plt.show()
# # #cv2.waitKey()
# # #cv2.destroyAllWindows()
# #
# # plt.show()
#
# #MORPHOLOGICAL OPERATIONS
# # import cv2
# # import numpy as np
# # from matplotlib import pyplot as plt
# # img=cv2.imread('gradient.png',cv2.IMREAD_GRAYSCALE)
# # #titles=['images']
# # images=[img]
# # for i in range(1):
# #    plt.subplot(1,1,i+1),plt.imshow(images[i],'gray')
# #  #  plt.title(titles[i])
# # plt.show()
#
#
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# img=cv2.imread('smarties.png',0)
#
# _, mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
# #NOW WE ARE USUNG DIALIATION TO FILL TAHT EMPTY SPOT/DOTS INSIDE THE BALL  IN MASK
# kernel=np.ones((2,2),np.uint8)
# #kernel=np.ones((5,5),np.uint8)     #zoom in the dilation screen  Either increase no of iterations or the zooming of the screen
# dilation=cv2.dilate(mask,kernel,iterations=1)
# erosion=cv2.erode(mask,kernel,iterations=1)
# opening=cv2.morphologyEx(mask ,cv2.MORPH_OPEN,kernel)
# closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
# mg=cv2.morphologyEx(mask ,cv2.MORPH_GRADIENT,kernel)
# mt=cv2.morphologyEx(mask ,cv2.MORPH_TOPHAT,kernel)
# #erosion followed by dilation is opening
# #dilation followed by erosion is closing
# #morphological gradient is the difference between erosion and dilation
# #tophat is the differnce between image and opening image
# titles=['imaggges','mask','dilation','erosion','opening','closing','MG','MT']
# iimages=[img,mask,dilation,erosion,opening,closing,mg,mt]
# for i in range(8):
#     plt.subplot(4,4,i+1),plt.imshow(iimages[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()











#already binary(black and white) type of image is there then we don't need to apply mask

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# img=cv2.imread('smarties.png',0)
#
# _, mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
# #NOW WE ARE USUNG DIALIATION TO FILL TAHT EMPTY SPOT/DOTS INSIDE THE BALL  IN MASK
# kernel=np.ones((2,2),np.uint8)
# #kernel=np.ones((5,5),np.uint8)     #zoom in the dilation screen  Either increase no of iterations or the zooming of the screen
# dilation=cv2.dilate(mask,kernel,iterations=1)
# erosion=cv2.erode(mask,kernel,iterations=1)
# opening=cv2.morphologyEx(mask ,cv2.MORPH_OPEN,kernel)
# closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
# mg=cv2.morphologyEx(mask ,cv2.MORPH_GRADIENT,kernel)
# mt=cv2.morphologyEx(mask ,cv2.MORPH_TOPHAT,kernel)
# #erosion followed by dilation is opening
# #dilation followed by erosion is closing
# #morphological gradient is the difference between erosion and dilation
# #tophat is the differnce between image and opening image
# titles=['imaggges','mask','dilation','erosion','opening','closing','MG','MT']
# iimages=[img,mask,dilation,erosion,opening,closing,mg,mt]
# for i in range(8):
#     plt.subplot(4,4,i+1),plt.imshow(iimages[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()











#SMOOTHING(REMOVING NOISES OR BLURRING) FROM IMAGES
#4 TYPES OF LINEAR FILTERS ARE USED
#LOW PASS FILTER REMOVE NOISES
#HIGH PASS FILTER ALSO REMOVE NOISES
#GAUSSIAN BLUR IS A BETTER FILTER THAN BLURFILTER.GAUSSIAN FILTER REMOVES HIGH FREQUENCY NOISES
#
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# img=cv2.imread('opencv-logo.png')
# img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  #it is necessary as we are using matplotlib
# kernel=np.ones((5,5),np.float32)/25
# dstimage=cv2.filter2D(img,-1,kernel,)
# blur=cv2.blur(img,(5,5))
# gblur=cv2.GaussianBlur(img,(5,5),0)
# median=cv2.medianBlur(img,5)       #here  u can only give odd size of kernel only except 1 #used to remove salt and pepper noises or like small white dots fro  images
# bilateral=cv2.bilateralFilter(img,9,75,75)            #used to maintain the edges sharply of an image
# titles=['images','2D Convolution','blur','gaussian blur','median','bilateral']
# images=[img,dstimage,blur,gblur,median,bilateral]
# for i in range(6):
#    plt.subplot(3,3,i+1),plt.imshow(images[i])
#    plt.title(titles[i])
#    plt.xticks([])
#    plt.yticks([])
# plt.show()











#GRADIENT FUNCTIONS(IMAGE GRADIENT AND EDGE DETECTION)

import cv2
import numpy as np
from matplotlib import pyplot as plt
#img=cv2.imread('opencv-logo.png')
#img=cv2.imread('messi5.jpg.png')
img=cv2.imread('sudoku.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  #it is necessary as we are using matplotlib
kernel=np.ones((5,5),np.float32)/25
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=1)    #datatype is 64 floattype and we have to convert back it's absolute value into unsignedinteger
lap=np.uint8(np.absolute(lap))
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1)
sobelX=np.uint8(np.absolute(sobelX))
sobely=np.uint8(np.absolute(sobely))
sobelcombined=cv2.bitwise_or(sobelX,sobely)
edges=cv2.Canny(img,100,200)              #for edge detection
images=[img,lap,sobelX,sobely,sobelcombined,edges]
titles=['image','Laplacian','SOBELX','SOBELY','SOBELCOMBINED','CANNY']
for i in range(6):
   plt.subplot(2,3,i+1),plt.imshow(images[i])
   plt.title(titles[i])
   plt.xticks([])
   plt.yticks([])
plt.show()
