import cv2
import numpy as np

frameW = 1080
frameH = 720

cap = cv2.VideoCapture(0)
#cap.set(3, frameW)
#cap.set(4, frameH)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameW, frameH))
    #imgCropped1 = img[0:100, 0:320]
    #imgCropped2 = img[0:500, 400:800]

    #Draw line
    cv2.line(img, (0,360), (1080,360), (0,0,255), 3)
    cv2.line(img, (540, 0), (540, 720), (0,0,255), 3)

    #Text
    cv2.putText(img, "Frame1", (80,200), cv2.FONT_HERSHEY_COMPLEX, 3, (0,255,255))
    cv2.putText(img, "Frame2", (600, 200), cv2.FONT_HERSHEY_COMPLEX, 3, (0,255,255))
    cv2.putText(img, "Frame3", (80, 550), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 255))
    cv2.putText(img, "Frame4", (600, 550), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 255))


    cv2.imshow("Cam Hik", img)
    #cv2.imshow("Cam Cropped1", imgCropped1)
    #cv2.imshow("Cam Cropped2", imgCropped2)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break