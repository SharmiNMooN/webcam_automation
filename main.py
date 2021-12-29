from types import GenericAlias
import cv2
import numpy as np
import pyautogui
cap = cv2.VideoCapture(0)
yellow_lower_red = np.array([22,93,50])
yellow_upper_red = np.array([45,255,255])
prev_y = 0
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yellow_lower_red, yellow_upper_red)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 300:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
            if y<prev_y:
                pyautogui.press('space')
            prev_y = y

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('q'):
        break
             
cap.release()
cv2.destroyAllWindows()