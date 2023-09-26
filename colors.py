import cv2
import numpy as np

def dibujar(mask, color):
    contours,_ =  cv2.findContours(mask, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
        area = cv2.contourArea(i)
        if area > 1000:
            new_countour = cv2.convexHull(i)
            cv2.drawContours(frame, [new_countour], 0, color, 3)

def captur():
    cap =  cv2.VideoCapture(1)
    low_yellow = np.array([25,192,20], np.uint8)
    high_yellow = np.array([30,255,255], np.uint8)
    low_red1 = np.array([0,100,20], np.uint8)
    high_red1 = np.array([5,255,255], np.uint8)
    low_red2 = np.array([175,100,20], np.uint8)
    high_red2 = np.array([180,255,255], np.uint8)


    while True:
        comp,frame =  cap.read()
        if comp == True:
            frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            yellow_mask = cv2.inRange(frame_hsv, low_yellow, high_yellow)
            red1_mask = cv2.inRange(frame_hsv, low_red1, high_red1)
            red2_mask = cv2.inRange(frame_hsv, low_red2, high_red2)
            # red_mask = cv2.inRange(frame_hsv, red1_mask, red2_mask)
            
            dibujar(yellow_mask, [0, 255, 255])
            dibujar(red1_mask, [0, 0 , 255])
            dibujar(red2_mask, [0, 0 , 255])
            
            cv2.imshow("Webcam", frame)
            
            """
            if cv2.waitKey(1) & 0xFF = ord("x"):
                break
                cap.release()
                cv2.destroyAllWindow()"""