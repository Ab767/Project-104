import cv2

img = cv2.imread("solar-system.jpg")

cv2.imshow("output",img)

cv2.putText(img, "Sun", (20, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(225,225,255) )

cv2.putText(img, "Mercury", (30, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(225,225,255) )

cv2.putText(img, "Venus", (50, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(225,225,255) )

cv2.putText(img, "Earth", (70, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(225,225,255) )

cv2.putText(img, "Mars", (90, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(225,225,255) )

cv2.putText(img, "Jupiter", (110, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(225,225,255) )

cv2.putText(img, "Saturn", (130, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(225,225,255) )

cv2.putText(img, "Uranus", (150, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(225,225,255) )

cv2.putText(img, "Neptune", (30, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(225,225,255) )

cv2.waitkey(0)
