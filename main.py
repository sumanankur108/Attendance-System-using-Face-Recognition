import cv2
import os

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
template_img = cv2.imread("Resources/background.png")
# resize_template_img = cv2.resize(template_img,(1180,680))

pathMode = 'Resources/Modes'
pathListMode = os.listdir(pathMode)
imgModeList = []
for i in pathListMode:
    full_path = os.path.join(pathMode,i)
    imgModeList.append(cv2.resize(cv2.imread(full_path),(413,673)))
# print(len(imgModeList))
# print(pathListMode)
# print(imgModeList[0].shape[0])
# print(imgModeList[0].shape[1])

while True:
    success, img = cap.read()
    # cv2.imshow("Face Attendance Webcam",img)
    template_img[162:162+480,55:55+640] = img
    img = cv2.imread("Resources/background.png")
    template_img[3:43+633, 840:840+413] = imgModeList[3]
    cv2.imshow("Template",template_img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.destroyAllWindows()