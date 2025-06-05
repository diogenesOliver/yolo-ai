class SleedDetection:
    def __init__(self):
        pass

    def process_frame(self, frame, model):
        results = model(frame)
        return frame