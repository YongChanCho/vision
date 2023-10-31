import cv2 as cv
import sys

img=cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.rectangle(img,(300,30),(500,200),(255,0,0),10) #색은 RGB순이 아닌 BGR
#인자 차례대로 (이미지,직사각형 왼쪽 위 좌표,직사각형 오른쪽 위 좌표,직사각형 색,직사각형 선 두께)
#다른 자세한 OpenCV 함수 정보는 공식 사이트 or 구글
cv.putText(img,'Playing hard mother fxxcker',(300,100),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv.imshow('Draw',img)

cv.waitKey()
cv.destroyAllWindows()