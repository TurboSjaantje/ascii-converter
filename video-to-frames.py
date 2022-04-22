import cv2
import os

# Opens the Video file
cap = cv2.VideoCapture('.\\parts\\video\\example.mp4')
i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite(os.path.join('./parts/frames','frame'+str(i)+'.jpg'), frame)
    i += 1

cap.release()
cv2.destroyAllWindows()

print('finished with splitting video into images!')

#-------------------------------------------------------------------

