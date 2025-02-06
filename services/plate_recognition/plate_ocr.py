import cv2
import easyocr
import os
import json


class PlateRecognitionOCR:
    def __init__(self):
        self.reader = easyocr.Reader(['pt']) 

    def apply_ocr_on_frame_plate(self, folder_path="records"):
        for file in os.listdir(folder_path):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                frame_path = os.path.join(folder_path, file)
                
                frame = cv2.imread(frame_path)
                result = self.reader.readtext(frame)

                if frame is None:
                    print(f"Erro: Não foi possível carregar a imagem '{file}'. Verifique o caminho.")
                    continue

                for bbox, text, conf in result:
                    plate_recognition_data = dict()

                    plate_recognition_data['text'] = text
                    plate_recognition_data['confiability'] = conf

                    plate_recognition_json = json.dumps(plate_recognition_data, indent=4)

                    print(plate_recognition_json)

        return "Done ."
    

PlateRecognitionOCR().apply_ocr_on_frame_plate()