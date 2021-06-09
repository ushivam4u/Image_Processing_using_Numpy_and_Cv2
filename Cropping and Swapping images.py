import cv2
import numpy
joker1 = cv2.imread("jj.jpg") #imported 1st joker image
joker2 = cv2.imread("joker.jpg")#imported 2nd joker image

joker1.shape #pixels of 1st image
joker2.shape ##pixels of 2nd image
j1=cv2.resize(joker1, [850, 600]) #Resizing 1st image
j2=cv2.resize(joker2, [850, 600]) #Resizing 2nd image
j1.shape # Pixels after resizing of 1st image
j2.shape #Pixels after resizing of 2nd image

# 1ST IMAGE
cv2.imshow("Joker 1", j1)
cv2.waitKey()
cv2.destroyAllWindows()

#2ND IMAGE
cv2.imshow("Joker 2 ", j2)
cv2.waitKey()
cv2.destroyAllWindows()

#CROPPED 1ST IMAGE
croppedj1left= j1[:, 0:400] #left side of Joker1
cv2.imshow("Joker1 cropped", croppedj1left)
cv2.waitKey()
cv2.destroyAllWindows()

#CROPPED 2ND IMAGE
croppedj2right= j2[:600, 425:850] # cropped right side of joker 2
cv2.imshow("Joker2 Cropped", croppedj2right)
cv2.waitKey()
cv2.destroyAllWindows()

#MERGED
swap1= numpy.hstack([croppedj1left, croppedj2right])
cv2.imshow("Swappaed and Merged 1", swap1)
cv2.waitKey()
cv2.destroyAllWindows()

#SWAPPED
croppedj1right= j1[:, 425:850] #right side of Joker1
croppedj2left= j2[:600, :425] #left side of joker 2
swap2= numpy.hstack([croppedj2left, croppedj1right])
cv2.imshow("Joker 1", swap2)
cv2.waitKey()
cv2.destroyAllWindows()
