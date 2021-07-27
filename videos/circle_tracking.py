import cv2
import numpy as np
from djitellopy import tello

my_drone = tello.Tello()
my_drone.connect()
my_drone.streamon()

'''while True:
    frame = my_drone.get_frame_read().frame
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        new = cv2.medianBlur(gray, 5)
        #newimg = cv2.cvtColor(new, cv2.COLOR_GRAY2BGR)

        circles = cv2.HoughCircles(new, cv2.HOUGH_GRADIENT, 1, 360, param1=100, param2=30, minRadius=0, maxRadius=250)
        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 3)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 10)

        cv2.imshow('Frame', frame)
        cv2.waitKey(0)'''

video_capture = cv2.VideoCapture(0)

while True:
    ret, img = video_capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    circles1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 360, param1=100, param2=30, minRadius=0, maxRadius=250)
    try:
        circles = circles1[0, :, :]
    except TypeError:
        print('NULL')
    else:
        circles = np.uint16(np.around(circles))
        for i in circles[:]:
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 3)
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 10)

    cv2.imshow('Video', img)
