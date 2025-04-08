import json
import argparse
import logging as logs

#from utils.yolo_model_handler import YoloModelHandler

with open('/home/diogenes/Documentos/www/yolo-ai/config.json') as f:
    config = json.load(f)

def main():
    parser = argparse.ArgumentParser(description='Video management with execution parameters')

    parser.add_argument('-b','--background', action='store_true', help='Running video in background')
    parser.add_argument('-r', '--realtime', action='store_true', help='Running video in real time')

    args = parser.parse_args()

    if args.realtime:
        print('[INFO] - Running in real time')
    
    if args.background:
        print('[INFO] - Running in background')

if __name__ == '__main__':

    main()