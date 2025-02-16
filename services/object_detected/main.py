from ultralytics import YOLO

class DetectVeicle:
    def __init__(self):
        self.model = YOLO('yolo/best.pt')
        pass

    def detect_object(self, video_path):
        results = self.model.predict(source=video_path, save=True, conf=0.4) 
        results.show()

        return "Done ."

if __name__ == "__main__":
    video_path = "records/transito.mp4"
    DetectVeicle().detect_object(video_path)