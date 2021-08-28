#!/usr/bin/env python3.6

import mediapipe as mp
import cv2
import numpy as np
import sys

if __name__ == "__main__":

    # Init mediapipe drawing and pose
    mp_drawing=mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    # Init Video Feed
    # Opens file if passed as parameter
    # Else Defaults to webcam
    cap=None
    if len(sys.argv) > 1:
        cap=cv2.VideoCapture(str(sys.argv[1]))
    else:
        cap=cv2.VideoCapture(0)

    while(cap.read()[1] is None):
        print("Waiting for Video")

    # Main Detection Loop
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame=cap.read()
            if ret == True:
    
                #Convert frame to RGB
                #Writeable = False forces pass by ref (faster)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame.flags.writeable = False

                #Detect Pose Landmarks
                landmarks = pose.process(frame).pose_landmarks
                
                #Draw overlay
                frame.flags.writeable = True
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                mp_drawing.draw_landmarks(frame, landmarks, mp_pose.POSE_CONNECTIONS)

                cv2.imshow("image", frame)
                cv2.waitKey(1)
            else:
                cap.release()
                break
