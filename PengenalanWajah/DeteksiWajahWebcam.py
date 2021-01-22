# install modul opencv : pip install opencv-contrib-python
# install modul pillow : pip install Pillow
# algoritma Haar-Cascade untuk mendeteksi wajah
# deteksi wajah https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# deteksi mata https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
# langkah untuk face recognition: rekam data wajah, training data wajah, recognition

import cv2
cam = cv2.VideoCapture(0)
cam.set(3, 640) # ubah lebar cam
cam.set(4, 480) # ubah tinggi cam
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    retV, frame = cam.read()
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(abuAbu, 1.3, 5)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,255), 2)
    cv2.imshow('Webcamku',frame)
    # cv2.imshow('Webcamku 2', abuAbu)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q') :
        break

cam.release()
cv2.destroyAllWindows()