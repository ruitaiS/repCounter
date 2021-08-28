import mediapipe as mp
import cv2
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


def process_frame(frame):
    print("Hi :)")


if __name__ == "__main__":

    # VideoCapture([Filename String]) for pre-recorded video
    # VideoCapture(0) pulls from integrated webcam
    #cap = cv2.VideoCapture(0)

    # Opens file if passed as parameter
    # Else Defaults to webcam
    cap = None
    if len(sys.argv) > 1:
        cap = cv2.VideoCapture(str(sys.argv[1]))
    else:
        cap = cv2.VideoCapture(0)

    while(cap.read()[1] is None):
        print("Waiting for Video")

    # Main Detection Loop
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
            cv2.imshow("image", frame)
            cv2.waitKey(1)
        else:
            cap.release()
            break
