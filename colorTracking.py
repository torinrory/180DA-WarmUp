# followed OpenCV object tracking tutorial at https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
# also used code from the contour features tutorial for the bounding box: https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
# https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html

# the range I needed to track the object was only from blue 90 to blue 120. I could get the range a little smaller but the tracking because a bit less reliable.
# making the environment brighter didn't change the tracking but making the room darker make it lose the object occasionally
# using the color picker on my phone, lower to medium brightness was better and it wasn't able to track higher brightness 

import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
	_, frame = cap.read()

	# converts from BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# BGR bounds for blue water bottle
	lower = np.array([90, 50, 50])
	upper = np.array([120, 255, 255])

	mask = cv2.inRange(hsv, lower, upper)

	# finds contours for bounding box
	contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	if contours:
		largest_contour = max(contours, key = cv2.contourArea)

		x, y, w, h = cv2.boundingRect(largest_contour)

		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

	cv2.imshow('frame', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()

cv2.destroyAllWindows()
