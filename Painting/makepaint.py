import cv2 as cv
import sys

img=cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

BrushSiz=5
LColor,RColor=(255,0,0)(0,0,255) 
#BGR 왼쪽 버튼 누르면 B=255이므로 B,오른쪽 버튼 누르면 R=255이므로 R 