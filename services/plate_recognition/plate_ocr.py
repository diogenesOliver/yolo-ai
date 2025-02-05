import yolov5
import cv2
import easyocr

class PlateRecognitionOCR:
    def __init__(self, model_path="keremberke/yolov5m-license-plate"):
        self.model = yolov5.load(model_path) 

        self.model.conf = 0.60  
        self.model.iou = 0.45  
        self.model.agnostic = False  
        self.model.multi_label = False  
        self.model.max_det = 1000

        self.reader = easyocr.Reader(['pt']) 

    def apply_ocr_on_frame_plate(self, frame):
        results = self.model(frame)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        for detection in results.pred[0]:
            x1, y1, x2, y2, conf, cls = detection.tolist()

            if conf >= 0.60:
                plate_region = frame_rgb[int(y1):int(y2), int(x1):int(x2)]

                ocr_results = self.reader.readtext(plate_region)
                plate_text = " ".join([result[1] for result in ocr_results])  

                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)  
                cv2.putText(frame, plate_text, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imwrite('results/frame5.jpg', frame)

        return "Process concluded"
    

frame = cv2.imread("records/frame5.jpg")
PlateRecognitionOCR().apply_ocr_on_frame_plate(frame)