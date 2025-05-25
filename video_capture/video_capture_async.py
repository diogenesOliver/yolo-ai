import os
import cv2
import json

from services.sleep_detection.main import SleedDetection

class VideoProcess:
    def __init__(self, video_name, target_size=(800, 600)):
        self.video_name = video_name
        self.target_size = target_size
        self.video_path = os.path.join('./records', video_name)

        pass

        self.json_file = "config.json"

        with open(self.json_file, 'r') as f:
            self.config = json.load(f)

    def open_video(self):
        if not os.path.exists(self.video_path):
            raise FileNotFoundError(f"Vídeo {self.video_name} não encontrado na pasta ./records.")

        self.cap = cv2.VideoCapture(self.video_path)
        if not self.cap.isOpened():
            raise Exception(f"Não foi possível abrir o vídeo {self.video_name}.")

        while True:
            ret, frame = self.cap.read()
            frame = cv2.resize(frame, self.target_size)

            if self.config['process']['service'][0]['application'] == "SleepDetector":
                SleedDetection().process_frame(frame)


            if not ret:
                break

            cv2.imshow("Video", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break