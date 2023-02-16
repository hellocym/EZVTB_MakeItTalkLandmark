import pyvirtualcam
import numpy as np
import cv2

def test():
    video = "./avconcat.mp4"
    cap = cv2.VideoCapture(video)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) // 3
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    with pyvirtualcam.Camera(width=w, height=h, fps=fps, device="Unity Video Capture") as cam:
        print(f'Using virtual camera: {cam.device}')
        frame = np.zeros((cam.height, cam.width, 3), np.uint8)  # RGB
        while True:
            ret, frame = cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)            # frame[:, :, 0] = cam.frames_sent % 255
            frame = frame[:, w:w*2]
            cam.send(frame)
            cam.sleep_until_next_frame()


if __name__ == '__main__':
    test()