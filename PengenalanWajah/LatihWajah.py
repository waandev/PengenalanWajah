import cv2, os, numpy as np
from PIL import Image

wajahDir = 'dataWajah'
latihDir = 'latihWajah'

def getImageLabel(path):
    imagePaths = [os.path.join(path,f) for  f in os.listdir(path)]
    faceSamples = []
    faceIDs = []
    for imagePath in imagePaths:
        PILImg = Image.open(imagePath).convert('L') # convert ke dalam gray
        imgNum = np.array(PILImg, 'uint8')
        faceID = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = faceDetector.detectMultiScale(imgNum)
        for (x, y, w, h) in faces:
            faceSamples.append(imgNum[y:y+h,x:x+w])
            faceIDs.append(faceID)
            return faceSamples, faceIDs

faceRecognizer = cv2.face.LBPHFaceRecognizer_create()
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

print("Mesin sedang melakukan training data wajah. Tunggu dalam beberapa detik.")
faces, IDs = getImageLabel(wajahDir)
faceRecognizer.train(faces, np.array(IDs))

# simpan
faceRecognizer.write(latihDir+'/training.xml')
print('Sebanyak {0} data wajah telah ditrainingkan ke mesin.',format(len(np.unique(IDs))))