import numpy as np
import cv2

if __name__ == '__main__':
    capture_device = cv2.VideoCapture(2)
    while (True):
        is_frame_captured, frame = capture_device.read()
        cv2.imshow('capture_device_feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture_device.release()
    cv2.destroyAllWindows()
