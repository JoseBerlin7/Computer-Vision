import cv2
import numpy as np
import streamlit as st
from matplotlib import pyplot as plt


def main():
    st.title("SIGNATURE EXTRACTOR")

    doc_upload =  st.file_uploader(label="Drop ur doc here", accept_multiple_files=True, type=['jpg', 'jpeg', 'png', 'webp'])

    for doc in doc_upload:
        doc_bytes = np.asarray(bytearray(doc.read()), dtype=np.uint8)
        img = cv2.imdecode(doc_bytes, 1)

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        _, thresh = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        contours =  sorted(contours, key=cv2.contourArea, reverse=True)

        x, y, w, h = cv2.boundingRect(contours[0])

        img_fin = img[y:y+h, x:x+w]

        st.image(img_fin, channels="BGR")

        cv2.imwrite(f"outputs/{doc.name}.jpg",img_fin)
        

if __name__ == "__main__":
    main()