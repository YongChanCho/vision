import cv2 as cv
import sys

img=cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

def draw(event,x,y,flags,param):    #콜백 함수
    global ix,iy

    if event==cv.EVENT_LBUTTONDOWN:   #마우스 왼쪽 클릭했을때
        ix,iy=x,y
    elif event==cv.EVENT_LBUTTONUP:
        cv.rectangle(img,(ix,iy),(x,y),(255,0,0),5)
    
    if event==cv.EVENT_RBUTTONDOWN:   #마우스 왼쪽 클릭했을때
        ix,iy=x,y
    elif event==cv.EVENT_RBUTTONUP:
        cv.rectangle(img,(ix,iy),(x,y),(0,0,255),5)
    
    cv.imshow('Drawing',img)

cv.namedWindow('Drawing')
cv.imshow('Drawing',img)

cv.setMouseCallback('Drawing',draw)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break