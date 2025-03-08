import cv2 
import mediapipe as mp
from ultralytics import YOLO

class SleedDetection:
    def __init__(self):
        self.model = YOLO("../../yolo/head_yolov8n.pt")
        pass

    def sleep_detection(self):
        """cap = cv2.VideoCapture("records/sleep_test.mp4")

        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break
            
            frame_resized = cv2.resize(frame, (640, 360))
            cv2.imshow("Sleep Detection", frame_resized)

            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

            return "Done .""
        """

        results = self.model.predict(source="records/sleep_test.mp4", save=True, conf=0.4)
        results.show()

        return "Done ."


SleedDetection().sleep_detection()