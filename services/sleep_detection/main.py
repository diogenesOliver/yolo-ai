import cv2 
import mediapipe as mp
from ultralytics import YOLO
import sys
import os

os.environ["QT_QPA_PLATFORM"] = "xcb"

class SleedDetection:
    def __init__(self):
        pass

    def process_frame(self):
        cap = cv2.VideoCapture("records/sleep_test.mp4")

        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            frame_resized = cv2.resize(frame, (640, 360))
            cv2.imshow("Sleep Detection", frame_resized)

            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
        return "Done ." 

"""if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-r":
        print("Running sleep detection")
        SleedDetection().sleep_detection()

SleedDetection().sleep_detection()"""