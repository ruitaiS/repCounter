#!/usr/bin/env python3.6

import mediapipe as mp
import cv2
import numpy as np
import sys

def findAngle(a, b, c, minVis = 0.1):
    #Finds the angle at b with endpoints a and c
    #Returns -1 if below minimum visibility threshold
    #Takes lm_arr elements

    if(a.visibility > minVis and b.visibility > minVis and c.visibility > minVis):
        bc = np.array([c.x - b.x, c.y - b.y, c.z - b.z])
        ab = np.array([b.x - a.x, b.y - a.y, b.z - a.z])

        return np.arccos((np.dot(ab, bc))/(np.linalg.norm(ab)*np.linalg.norm(bc)))
    else:
        return -1

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
                #lm used for drawing
                #lm_arr is actually indexable with .x, .y, .z attr
                lm = pose.process(frame).pose_landmarks
                lm_arr = lm.landmark
                
                #Allow write, convert back to BGR
                frame.flags.writeable = True
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)


                #Draw overlay with parameters:
                #(frame, landmarks, list of connected landmarks, landmark draw spec, connection draw spec)
                mp_drawing.draw_landmarks(frame, lm, mp_pose.POSE_CONNECTIONS, mp_drawing.DrawingSpec(color=(0,255,0), thickness = 2, circle_radius = 2), mp_drawing.DrawingSpec(color=(0,0,255), thickness = 2, circle_radius = 2))

                #Calculate Angle
                try:
                    print(findAngle(lm_arr[16],lm_arr[14], lm_arr[12])*(180/3.14))
                except:
                    print("Err")


                cv2.imshow("image", frame)
                cv2.waitKey(1)
            else:
                cap.release()
                break
