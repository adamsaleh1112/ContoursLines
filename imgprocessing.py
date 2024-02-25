import cv2
import numpy as np

def processed(img, maskx, masky, maskw, maskh):

    # PROCESSING
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray, (3, 3))
    edges = cv2.Canny(blur, 50, 150, apertureSize=3)

    # MASK VARIABLES
    x = maskx
    y = masky
    w = maskw
    h = maskh
    mask = np.zeros(edges.shape[:2], np.uint8)
    mask[y:y + h, x:x + w] = 255
    maskimg = cv2.bitwise_and(edges, edges, mask=mask)

    return maskimg

# PROGRAMMING WORKS CITED

# Masking (Lines 18-25): https://stackoverflow.com/questions/11492214/opencv-via-python-is-there-a-fast-way-to-zero-pixels-outside-a-set-of-rectangle