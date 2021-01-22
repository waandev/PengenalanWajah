# install modul opencv : pip install opencv-contrib-python
# install modul pillow : pip install Pillow
# algoritma Haar-Cascade untuk mendeteksi wajah
# deteksi wajah https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# deteksi mata https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml

import cv2
cam = cv2.VideoCapture(0)
while True:
    retV, frame = cam.read()
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Webcamku',frame)
    cv2.imshow('Webcamku 2', abuAbu)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q') :
        break

cam.release()
cv2.destroyAllWindows()