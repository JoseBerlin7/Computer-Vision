# Purpose: to detect all the faces and eyes in the cam
import cv2
import argparse

# Args
parser = argparse.ArgumentParser(description="Cascade Classifier for openCV")
parser.add_argument("--detect_face", default="exercises/haar_face_detection/model/haarcascade_frontalface_default.xml")
parser.add_argument("--detect_eyes", default="exercises\haar_face_detection\model\haarcascade_eye_tree_eyeglasses.xml")
args = parser.parse_args()

cam = cv2.VideoCapture(0)

face_model = cv2.CascadeClassifier(args.detect_face)
eye_model = cv2.CascadeClassifier(args.detect_eyes)


while cam.isOpened():
    ret, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coods = face_model.detectMultiScale(gray, 1.1, 5)

    for (x,y,w,h) in face_coods:
        cv2.rectangle(frame, (x, y), (x+w,y+h), (255,0,0), 2)

        face = gray[y:y+h, x:x+w]

        eye_coods = eye_model.detectMultiScale(face, 1.3, 5)
        for (x1, y1, w1, h1) in eye_coods:
            eye_center = (x1+x+w1//2, y+y1+h1//2)
            radius = int(round(w1+h1)*0.10)
            cv2.circle(img=frame, center=eye_center, radius=radius, color=(0,255,255))

    cv2.imshow("Me", frame)

    if cv2.waitKey(4) & 0XFF == ord('q'):
        break