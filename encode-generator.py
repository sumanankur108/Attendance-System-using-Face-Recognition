import os
import cv2
import face_recognition
import pickle

# Importing student images
imgPath = "Images"
imgTitleList = os.listdir(imgPath)
print(imgTitleList)
# List for storing the images
imgList = []
# List for storing student IDs
studentIDs = []
for i in imgTitleList:
    imgList.append(cv2.imread(os.path.join(imgPath,i)))
    # studentIDs.append(i.split('.')[0])
    studentIDs.append(os.path.splitext(i)[0])
print(len(imgList))
print(studentIDs)

def findEncodings(imagesList):
    encodeList = []
    for i in imagesList:
        i = cv2.cvtColor(i,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(i)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started!")
encodeListKnown = findEncodings(imgList)
print(encodeListKnown)
encodeListKnownWithIDs = [encodeListKnown,studentIDs]
print("Encoding Complete!")

file = open("encode-file.p", 'wb')
pickle.dump(encodeListKnownWithIDs,file)
file.close()