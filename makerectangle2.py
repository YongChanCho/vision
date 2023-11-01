import cv2 as cv
import sys

img=cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

def draw(event,x,y,flags,param):    #콜백 함수
    if event==cv.EVENT_LBUTTONDOWN:   #마우스 왼쪽 클릭했을때
        cv.rectangle(img,(x,y),(x+200,y+200),(0,0,255),5)
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img,(x,y),(x+200,y+200),(255,0,0),5)
    
    cv.imshow('Drawing',img)

# cv.namedWindow('Drawing')
cv.imshow('Drawing',img)

cv.setMouseCallback('Drawing',draw)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break