import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
webcam = cv2.VideoCapture(0)
webcam.set(3, 640)
webcam.set(4, 380)
webcam.set(10, 100)

while webcam.isOpened():
    success, frame = webcam.read()

    if success:

        # Word Detection
        boxes = pytesseract.image_to_data(frame)
        for x, box in enumerate(boxes.splitlines()):
            if x != 0:
                box = box.split()
                print(box)
                if len(box) == 12:
                    x, y, w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
                    cv2.rectangle(frame, (x, y), (w + x, h + y), (0, 255, 0), 2)
                    cv2.putText(frame, box[11], (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Image", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

webcam.release()
cv2.destroyAllWindows()

