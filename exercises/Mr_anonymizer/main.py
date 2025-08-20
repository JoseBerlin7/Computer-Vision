import cv2
import mediapipe as mp

def process_face(frame, face_detection):
    out = face_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    W, H, _ = frame.shape

    if out.detections is not None:
         for detection in out.detections:
              bbox = detection.location_data.relative_bounding_box

              x, y, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

              x = int(x*W)
              y = int(y*H)
              w = int(w*W)
              h = int(h*H)

              frame[y:y+w, x:x+h, :] = cv2.blur(frame[y:y+w, x:x+h, :], (30,30))
              
              return frame


def main():
    cam = cv2.VideoCapture(0)
    
    while cam.isOpened():
        ret, frame = cam.read()

        mp_face_detect =  mp.solutions.face_detection

        with mp_face_detect.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
            img = process_face(frame, face_detection)
            cv2.imshow("Hello",img)

            if cv2.waitKey(4) & 0xFF == ord('q'):
                break

    cam.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()

        


