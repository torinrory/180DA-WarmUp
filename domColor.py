# followed given tutorial from: https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
# phone is must less robust when it comes to brightness changes. The water bottle's color stays pretty consistent

import cv2
import numpy as np
from sklearn.cluster import KMeans

def findDomColor(image, k = 1):

    pixels = image.reshape(-1, 3)

    # fits k-means algorithm to pixels
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)

    # gets cluster centers for dominant color
    domColor = kmeans.cluster_centers_[0].astype(int)

    return domColor

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # defines area that we want to find dominant color
    rectStart = (500, 300)
    rectEnd = (700, 500)

    rect = frame[rectStart[1]:rectEnd[1], rectStart[0]:rectEnd[0]]

    # finds the dominant color using k-means
    domColor = findDomColor(rect, k = 1)

    # displays area that is being processed
    cv2.rectangle(frame, rectStart, rectEnd, (0, 255, 0), 2)
    frame[rectStart[1]:rectEnd[1], rectStart[0]:rectEnd[0]] = domColor

    # displays frame with highlighted area and dominant color
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
