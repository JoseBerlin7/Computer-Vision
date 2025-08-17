import cv2 
import os

vid = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp42')
out = cv2.VideoWriter(os.path.join('vids', 'output.mp4'), fourcc, 20.0, (640,480))

while vid.isOpened():
    ret, frame = vid.read()
    if not ret:
        break
    out.write(frame)

    cv2.imshow('Video Feed', frame)

    if cv2.waitKey(6) & 0xFF == ord('q'):
        break

vid.release()
out.release()
cv2.destroyAllWindows()