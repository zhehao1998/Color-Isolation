import numpy as np
import cv2

def empty(a):
    pass


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 600, 340)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)


while True:
    img_rgb = cv2.imread("example.jpg")
    dim = img_rgb.shape
    trim = 5  # px trim to get rid of black edge box
    img_rgb = img_rgb[trim:dim[0]-trim, trim:dim[1]-trim,:]
    img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    lower = np.array([h_min, sat_min, val_min])
    upper = np.array([h_max, sat_max, val_max])

    mask = cv2.inRange(img_hsv, lower, upper)
    masked = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow("Original", img_rgb)
    # cv2.imshow("HSV", img_hsv)
    # cv2.imshow("Mask", mask)
    cv2.imshow("Masked", masked)
    cv2.waitKey(1)

cv2.destroyAllWindows()
