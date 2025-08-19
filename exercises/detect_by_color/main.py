import cv2
from utils import get_hsv_color_range
from PIL import Image

def main():
    yellow = [0, 255, 255]  # BGR format for yellow
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        l, u = get_hsv_color_range(yellow)
        mask = cv2.inRange(hsv_frame, l, u)

        # Apply the mask to the original frame
        mask_ = Image.fromarray(mask)

        bbox = mask_.getbbox()

        if bbox:
            x, y, w, h = bbox
            cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 5)

        cv2.imshow('Original Frame', frame)

        cv2.imshow('Webcam Feed', mask)

        if cv2.waitKey(4) & 0xFF == ord('q'):
            break

        if not ret:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()