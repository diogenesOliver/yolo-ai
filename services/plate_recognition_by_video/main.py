import yolov5
import cv2
import easyocr
import os

class PlateRecognitionByVideo:
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
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        for detection in results.pred[0]:
            x1, y1, x2, y2, conf, cls = detection.tolist()

            plate_region = frame_rgb[int(y1):int(y2), int(x1):int(x2)]

            ocr_results = self.reader.readtext(plate_region)
            plate_text = " ".join([result[1] for result in ocr_results]) 

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2) 
            cv2.putText(frame, plate_text, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            
            print(f"This is conf level: {conf}")

        results.show()        
        return frame
    

    @staticmethod
    def process_video(video_path, output_path):
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Erro: Não foi possível abrir o vídeo '{video_path}'.")
            return

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            processed_frame = PlateRecognitionByVideo().process_frame(frame)

            cv2.imshow("Processed Video", processed_frame)

            out.write(processed_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()

        print(f"Vídeo processado salvo em: {output_path}")

if __name__ == "__main__":
    
    input_video = "records/1.mp4"
    output_video = "results/processed_video.mp4"

    plate_recognition = PlateRecognitionByVideo()

    plate_recognition.process_video(input_video, output_video)