import cv2

img = cv2.imread("Resources/background.png")
img[3:43+633, 840:840+413] = cv2.resize(cv2.imread("Resources/Modes/1.png"), (413, 673))
cv2.imshow("Display",img)
cv2.waitKey(0)
cv2.destroyAllWindows()