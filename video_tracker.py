import numpy as np
import cv2 as cv
import time
import os
from ultralytics import YOLO

# set up the folder that we put frames into
output_folder = "captured_frames"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

interval = 3
last_capture_time = time.time()


cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    current_time = time.time()
    #check if 3 seconds have passed
    if current_time - last_capture_time >= 3:
        filename = os.path.join(output_folder, f"frame_{int(current_time)}.jpg")
        cv.imwrite(filename, frame)
        print("Frame captured!")
        last_capture_time = current_time
    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()