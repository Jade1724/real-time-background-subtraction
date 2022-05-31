'''
Video preproccessing for COSC428 real-time background subtraction project
Specify the source video and distination video (only .mp4 supported) to perform image resizing and smoothing.
Recommended frame resolution is 512 x 512 to achieve real-time background subtraction.
'''

import cv2
import numpy as np

path = "videos/original_videos/vr-player.mp4"
cap = cv2.VideoCapture(path)


resolution = (640, 360)    # Used for resizing videos/original-videos/vr-player.mp4
# resolution = (768, 432)    # Used for resizing videos/original-videos/vr-player2.mp4
# resolution = (432, 768)    # Used for resizing videos/original-videos/vr-player-3.mp4

fps = round(cap.get(cv2.CAP_PROP_FPS))
# print(fps)
out = cv2.VideoWriter('videos/preprocessed_videos/vr-player-resized.mp4',  cv2.VideoWriter_fourcc(*"mp4v"), fps, resolution)

while True:
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, resolution)

        height, width, _ = frame.shape

        frame = cv2.GaussianBlur(frame,(1,1),0)

        out.write(frame)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()