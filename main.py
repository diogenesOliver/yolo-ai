import json

with open('/home/diogenes/Documentos/www/yolo-ai/config.json') as f:
    config = json.load(f)

if config['process']['service'] == 'sleepDetector':
    from services.sleep_detection.main import SleedDetection
    SleedDetection().sleep_detection()
else:
    print("Invalid service .")

if __name__ == "__main__":
    print("running main.py")
    pass