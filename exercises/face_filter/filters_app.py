'''Idea: To create a instagram style photo filter in OpenCV
4 EFFECTS WE'RE PROVIDING
    # Gray
    # Sepia
    # Negative
    # Cartoon
    # Blur'''

import cv2
import numpy as np

class effects:
    def __init__(self):
        pass

    def gray(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    def serpia(self, img):
        kernal = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        serpia = cv2.transform(img, kernal)
        serpia = np.clip(serpia, 0, 255)

        return serpia

    def negative(self, img):

        return cv2.bitwise_not(img)
    
    def cartoon(self, img):

        gray = self.gray(img)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(img, 9, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        return cartoon
    
    def blur(self, img):

        return cv2.blur(img, (20,20), 0)
    

def main():
    cam = cv2.VideoCapture(0)

    while cam.isOpened():

        ret, frame = cam.read()
        c = effects()
        # img = c.gray(frame)
        # img = c.negative(frame)
        # img = c.blur(frame)
        img = c.serpia(frame)
        # img = c.cartoon(frame)

        cv2.imshow("Hello", img)

        if cv2.waitKey(3) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    # pass

if __name__ == "__main__":
    main()