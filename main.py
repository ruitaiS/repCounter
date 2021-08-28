import mediapipe as mp
import cv2
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

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

    # Use first frame to init Feature Extractor
    # F is some kinda parameter in the intrinsic Matrix, not sure
    while(cap.read()[1] is None):
        print("Waiting for Video")
    fe = FeatureExtractor(cap.read()[1], F=1)

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
