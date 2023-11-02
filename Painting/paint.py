import cv2 as cv
import sys

img=cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

BrushSize=5
LColor,RColor=(255,0,0),(0,0,255)

def painting(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),BrushSize,LColor,-1) #마우스 왼쪽 클릭하면 파란색
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.circle(img,(x,y),BrushSize,RColor,-1) #마우스 오른쪽 클릭하면 빨간색
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        cv.circle(img,(x,y),BrushSize,LColor,-1) #왼쪽 클릭하고 이동하면 파란색
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
        cv.circle(img,(x,y),BrushSize,RColor,-1) #오른쪽 클릭하고 이동하면 빨간색

    cv.imshow('Painting',img)

cv.namedWindow('Painting')
cv.imshow('Painting',img)

cv.setMouseCallback('Painting',painting)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break

