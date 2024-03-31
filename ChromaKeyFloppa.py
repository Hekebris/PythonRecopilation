import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)
verde_bajo = np.array([0, 150, 150])
verde_alto = np.array([150, 255, 255])

image = cv2.imread('floppa.jpg')
image_resized = cv2.resize(image, (640, 480))

while True:

    ret, frame = cap.read()

    if ret:

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, verde_bajo, verde_alto)

        mask_inv = cv2.bitwise_not(mask)

        frame_bg = cv2.bitwise_and(frame, frame, mask=mask_inv)

        bg_fg = cv2.bitwise_and(image_resized, image_resized, mask=mask)

        result = cv2.add(frame_bg, bg_fg)

        cv2.imshow('Video resultante', result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
