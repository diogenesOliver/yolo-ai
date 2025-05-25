import json
import argparse
import os

from video_capture.video_capture_async import VideoProcess
from process.main import ServiceProcess

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
        video_application = config['process']['service'][0]['application']

        if os.path.exists(records_path):
            for file in os.listdir(records_path):
                pwd_file = os.path.join(records_path, file)

                if os.path.isfile(pwd_file):
                    file = int(os.path.splitext(file)[0])
                    
                    if file == video_id:
                        video_name = f"{file}.mp4"
                        print("[INFO] - Video processing started")
                        
                        frame_generator = VideoProcess(video_name).open_video()
                        ServiceProcess().initialize_process(video_application, config, frame_generator)

                        return

    if args.background:
        print('[INFO] - Running in background')

if __name__ == '__main__':
    main()