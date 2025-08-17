import cv2
import numpy as np
import os 

def show_image(img, title='Image'):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save_image(img, filename):
    cv2.imwrite(os.path.join('processed','imgs', filename), img)

def main():
    img_path = os.path.join('imgs','dog.jpg')
    img = cv2.imread(img_path)

    if img is None:
        raise FileNotFoundError(f"Image not found at {img_path}")
    img = cv2.resize(img, (620, 480))


    # Display the original image
    # show_image(img)


    # Convert to grayscale 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_color = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # show_image(img_color)
    # save_image(img_gray, 'dog_gray.jpg')


    # adding blurring effects
    img_blur = cv2.GaussianBlur(img, (5, 1), 0)
    # show_image(img_blur)

    img_blur = cv2.blur(img, (1, 5), 0)
    # show_image(img_blur)

    img_blur = cv2.medianBlur(img, 7)
    # show_image(img_blur)
    # save_image(img_blur, 'dog_medianBlur.jpg')

    img_blur = cv2.bilateralFilter(img, 8, 75, 75)
    # show_image(img_blur)
    # save_image(img_blur, 'dog_bilateralFilter.jpg')


    # rotating the image
    img_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    # show_image(img_rotated)
    # save_image(img_rotated, 'dog_rotate90.jpg')

    # flipping the image
    img_flipped = cv2.flip(img,1)
    # show_image(img_flipped)
    # save_image(img_flipped, 'dog_flippedH.jpg')

    # Thresholding
    _, img_thres = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
    # show_image(img_thres)

    adap_thres = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 8)
    # show_image(adap_thres)


main()