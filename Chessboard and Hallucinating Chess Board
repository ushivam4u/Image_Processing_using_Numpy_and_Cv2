#CHESSBOARD
import numpy
import cv2
np = numpy.zeros((1000,1000)) #Created image of 1000x1000 pixels 
cb=0
cw=1
r1=0
c1=125
for i in range(0,8):
    r=0
    c=125
    for j in range(0,8):
        if i%2==0:
            if j%2==0:
                np[r:c, r1:c1]=[cw]
            else:
                np[r:c, r1:c1]=[cb]
        else:
            if j%2==0:
                np[r:c, r1:c1]=[cb]
            else:
                np[r:c, r1:c1]=[cw]
        r=r+125
        c=c+125
    r1=r1+125
    c1=c1+125
np1= numpy.zeros((1000,1000))
cb=0
cw=1
r1=0
c1=125
for i in range(0,8):
    r=0
    c=125
    for j in range(0,8):
        if i%2==0:
            if j%2==0:
                np1[r:c, r1:c1]=[cb]
            else:
                np1[r:c, r1:c1]=[cw]
        else:
            if j%2==0:
                np1[r:c, r1:c1]=[cw]
            else:
                np1[r:c, r1:c1]=[cb]
        r=r+125
        c=c+125
    r1=r1+125
    c1=c1+125
cv2.imshow("hi", np)
cv2.waitKey()
cv2.destroyAllWindows()

#HALLUCINATING CHESS BOARD

i=0
while True:
    if i%2==0:
        cv2.imshow("Halucinating Chess Board", np)
        if cv2.waitKey(100)== 13:
            break
    else:
        cv2.imshow("Halucinating Chess Board", np1)
        if cv2.waitKey(100)== 13:
            break
    i=i+1
cv2.destroyAllWindows()
