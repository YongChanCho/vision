import cv2 as cv
import sys

img=cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray_small=cv.resize(gray,dsize=(0,0),fx=0.5,fy=0.5) #반으로 축소

cv.imwrite('soccer_gray.jpg',gray)  #영상을 파일에 저장
cv.imwrite('soccer_gray_small.jpg',gray_small)  #영상을 파일에 저장

cv.imshow('Color image',img)
cv.imshow('Gray image',gray)
cv.imshow('Gray image_small',gray_small)

cv.waitKey()
cv.destroyAllWindows()