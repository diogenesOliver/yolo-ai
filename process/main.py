from utils.yolo_model_handler import YOLOModelHandler
from services.sleep_detection import SleepingDetectionService

import logging

class RealTime:
    def __init__(self, models: YOLOModelHandler):
        self.models = models
        
        pass

    def initialize_process(self, config):
        try:
            if config['process']['service'] == 'sleepDetector':
                self.sleeping_detection = SleepingDetectionService()

        except Exception as e:
            logging.error(f'21 - Erro: {e}')

    def change_frame(self, frame, config):
        try:
            if config['process']['service'] == "sleepDetector":
                frame = self.sleeping_detection.process_frame(frame, self.models.sleeping_detection, config)
        except Exception as e:
            logging.error(f'30 - Erro: {e}')