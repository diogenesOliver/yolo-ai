from ultralytics import YOLO
import torch

class YOLOModelHandler:
    def __init__(self):
        if torch.cuda.is_available():
            self.device = torch.device('cuda')
        else:
            self.device = torch.device('cpu')

        self.sleeping_detection = YOLO('./yolo/head_yolov8n.pt').to(self.device)