import json
import argparse
import os

from utils.yolo_model_handler import YOLOModelHandler
from video_capture.video_capture_async import VideoProcess

json_file = "config.json"

with open(json_file, 'r') as f:
    config = json.load(f)

def main():
    parser = argparse.ArgumentParser(description='Video management with execution parameters')

    parser.add_argument('-b','--background', action='store_true', help='Running video in background')
    parser.add_argument('-r', '--realtime', action='store_true', help='Running video in real time')

    args = parser.parse_args()

    if args.realtime:
        records_path = './records'
        video_id = config['process']['service'][0]['video_id']

        if os.path.exists(records_path):
            for file in os.listdir(records_path):
                pwd_file = os.path.join(records_path, file)

                if os.path.isfile(pwd_file):
                    file = int(os.path.splitext(file)[0])
                    
                    if file == video_id:
                        # Apply logic to process the video

                        return
                    else:
                        print("[ERROR] - No video file found")
                        return

    if args.background:
        print('[INFO] - Running in background')

if __name__ == '__main__':
    main()