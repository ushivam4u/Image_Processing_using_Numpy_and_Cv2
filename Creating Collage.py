import cv2
import numpy
hanuman = cv2.imread("hanuman.jpg") #imported 1st image
shiva = cv2.imread("lord.jpg") #imported 2nd image
hanuman.shape #pixels of 1st image
h=cv2.resize(hanuman,[564,831]) #resizing 1st image to match 2nd image

# 1ST IMAGE
cv2.imshow("Hanuman ", h)
cv2.waitKey()
cv2.destroyAllWindows()

# 2ND IMAGE
cv2.imshow("Shiva", shiva)
cv2.waitKey()
cv2.destroyAllWindows()
shiva.shape #pixels of 2nd image
h.shape #pixels of 1st image after resizing
merge = numpy.hstack([shiva, h]) #merging both images
coll= cv2.line(merge, (560,0), (560,831), (255,0,0), 20) #creating collage

#COLLAGE
cv2.imshow("Collage", coll)
cv2.waitKey()
cv2.destroyAllWindows()
