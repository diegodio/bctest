import cv2
import numpy as np
import streamlit as st

image = st.camera_input("Show QR code")

if image is not None:
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    detector = cv2.barcode.BarcodeDetector()

    decoded_info, decoded_type, points = detector.detectAndDecode(cv2_img)

    st.write("Here!")
    # st.write(data)

    if len(decoded_info) > 0:
        st.write('dasda')

        for info, type, points in zip(decoded_info, decoded_type, points):
            st.write(f"Barcode Type: {type}")
            st.write(f"Barcode Data: {info}")
            # Draw a rectangle around the barcode
            cv2.rectangle(img, points[0], points[2], (0, 255, 0), 2)
    else:
        st.write("No barcode found")


# if image is not None:
#     bytes_data = image.getvalue()
#     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

#     detector = cv2.QRCodeDetector()

#     data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

#     st.write("Here!")
#     st.write(data)

