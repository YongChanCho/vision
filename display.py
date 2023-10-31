import cv2 as cv #cv2모듈을 불러와 cv라는 이름으로 사용
import sys  #시스템 변수 설정이나 exit 함수로 프로그램 종료하는데 사용

img=cv.imread('soccer.jpg')   #cv2 모듈의 imread 함수(영상 읽기)
print(img[0,0]) #(x,y,z)축 중 (0,0,R) (0,0,G) (0,0,B) R,G,B 출력

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.imshow('Image Display Soccer',img)   #첫번째 인수는 윈도우 이름,두번째 인수는 윈도우에 디스플레이할 영상

#아래 waitKey가 없으면 윈도우 생성 후 프로그램 즉시 종료되어 못봄
cv.waitKey(5000)   #인수 없으면 키보드의 키가 눌릴 때까지 wait(이건 5000밀리초(5초)wait)
cv.destroyAllWindows()  #모든 윈도우 종료