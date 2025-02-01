import yolov5
import cv2
import easyocr
import os

class PlateRecognition:
    def __init__(self, model_path="keremberke/yolov5m-license-plate"):
        self.model = yolov5.load(model_path)
        
        self.model.conf = 0.25 
        self.model.iou = 0.45  
        self.model.agnostic = False  
        self.model.multi_label = False
        self.model.max_det = 1000

        self.reader = easyocr.Reader(['pt'])

    def process_frame(self, frame):
        results = self.model(frame, size=640)        
        
        for detection in results.pred[0]:
            x1, y1, x2, y2, conf, cls = detection.tolist()
            print(f"This is conf level: {conf}")

        results.show()

        cv2.waitKey(1000)
        cv2.destroyAllWindows()
        
        return frame
        """frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        for detection in results.pred[0]:
            x1, y1, x2, y2, conf, cls = detection.tolist()

            plate_region = frame_rgb[int(y1):int(y2), int(x1):int(x2)]

            ocr_results = self.reader.readtext(plate_region)
            plate_text = " ".join([result[1] for result in ocr_results])  

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)  
            cv2.putText(frame, plate_text, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow("Plate Recognition", frame)
        cv2.waitKey(0)

        cv2.imwrite('results/plate_recognized.jpg', frame)

        return "Process concluded"
        """
    
    @staticmethod
    def process_image_in_folder(folder_path, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        plate_recognition = PlateRecognition()

        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_path = os.path.join(folder_path, filename)
                frame = cv2.imread(image_path)

                if frame is None:
                    print(f"Erro: Não foi possível carregar a imagem '{filename}'. Verifique o caminho.")
                    continue

                processed_frame = plate_recognition.process_frame(frame)
                
                output_path = os.path.join(output_folder, filename)
                cv2.imwrite(output_path, processed_frame)

                print(f"Image processed: {output_path}")


if __name__ == "__main__":
    input_folder = "records"
    output_folder = "results"

    plate_recognition = PlateRecognition()
    plate_recognition.process_image_in_folder(input_folder, output_folder)