import cv2 as cv

img = cv.imread('floppa.png',cv.IMREAD_UNCHANGED)
orig_height, orig_width = img.shape[:2]
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascPath)
video_capture = cv.VideoCapture(0, cv.CAP_DSHOW)
anterior = 0

if not video_capture.isOpened():
    print('No se pudo acceder a la cámara')
else:
    while True:

        ret, frame = video_capture.read()
        frame = cv.flip(frame, 1)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:

            iresize = cv.resize(img, (w, h))
            transp_s = iresize[:, :, 3] / 255.0
            transp_l = 1.0 - transp_s 
            for c in range(0, 3):
                frame[y:y+h, x:x+w, c] = (transp_s * iresize[:, :, c] +
                                           transp_l * frame[y:y+h, x:x+w, c])
        cv.imshow('Video', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()

    cv.destroyAllWindows()


