import keyboard
from Gaze_Model.gaze_tracking.eyes_model import EyesModel
from Gaze_Model.Face_Detection.Face_Detection import DetectFace
import cv2
import time

if __name__ == '__main__':
    # Detect 1P face
    _1P_Face = DetectFace("1P")
    for count in range(50):
        if cv2.waitKey(1) == ord('q'):
            break
        _1P_Face.open(1 + count // 6)
        time.sleep(0.001)
    _1P_Face.capture("Person_1.png")
    _1P_Face = None
    print("1P Gacha")
    # Detect 2P face
    _2P_Face = DetectFace("2P")
    for count in range(50):
        if cv2.waitKey(1) == ord('q'):
            break
        _2P_Face.open(1 + count // 6)
        time.sleep(0.001)
    _2P_Face.capture("Person_2.png")
    _2P_Face = None
    print("2P Gacha")