# IMPORT NUMPY AND CV2
import numpy as np # importing numpy, a library that allows for complex data structures
import cv2 # importing opencv, a image processing library for python
from imgprocessing import processed # importing processing function

# VIDEO = VIDEO CAPTURE
vid = cv2.VideoCapture(0) # setting vid equal to index 0 capture (default webcam)

# WHILE TRUE
while (True): # indefinite loop

    # IMAGE PROCESSING
    ret, img = vid.read() # img or (frame) is equal to the frame being read

    maskx = 150 # mask variables
    masky = 100
    maskw = 350
    maskh = 250

    maskimg = processed(img=img, maskx=maskx, masky=masky, maskw=maskw, maskh=maskh) # image processing function

    contours, hierarchy = cv2.findContours(maskimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # detecting contour lines

    if contours is not None and len(contours) >= 2: # if there are atleast two contour lines detected

        midline = [] # defining an array for me to store the midpoints values for later

        contours = sorted(contours, key=cv2.contourArea, reverse=False) # sorting the contours by area so bigger will be the outer curve and smaller will be the inner curve
        contour1 = contours[0] # smallest (inner) contour
        contour2 = contours[-1] # biggest (outer) contour

        cv2.polylines(img, [np.array(contour1)], False, (255, 0, 0), 3)
        cv2.polylines(img, [np.array(contour2)], False, (0, 0, 255), 3)

        for i in range(min(len(contour1), len(contour2))):
            xavg = (contour1[i][0][0] + contour2[i][0][0]) / 2
            xavg = int(xavg)
            yavg = (contour1[i][0][1] + contour2[i][0][1]) / 2
            yavg = int(yavg)

            midline.append((xavg, yavg))

        # POLYLINES CONNECT ARRAY
        midline = np.array(midline)
        cv2.polylines(img, [np.array(midline)], False, (0, 255, 0), 3)

        # HIGHLIGHT MASK WITH RECTANGLE
        cv2.rectangle(img, (maskx, masky), (maskx + maskw, masky + maskh), (255, 255, 255), 3)

        # SHOW IMAGE
        cv2.imshow('frame', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# PROGRAMMING WORKS CITED

# Video capture and video display (Lines 1-13, 55-63) https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
# OpenCV rectangle (Line 48) https://www.geeksforgeeks.org/python-opencv-cv2-rectangle-method/
# OpenCV contours (Lines 22) https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
# Contour area (Line 28) https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
# Polylines (Line 45) https://www.geeksforgeeks.org/python-opencv-cv2-polylines-method/
# Sorting (Line 28) https://docs.python.org/3/howto/sorting.html
