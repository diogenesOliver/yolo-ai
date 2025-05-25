from utils.yolo_model_handler import YOLOModelHandler
from services.sleep_detection.main import SleedDetection

import logging

class ServiceProcess:
    def __init__(self):
        pass

    async def initialize_process(self, video_application, config, frame):
        try:
            if video_application == 'SleepDetector':
                self.sleeping_detection = await SleedDetection(config).process_frame(frame)
        
        except Exception as e:
            logging.error(f'- Process incialization error: {e}')