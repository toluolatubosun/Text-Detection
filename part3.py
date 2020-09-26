import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('Text.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Word Detection
boxes = pytesseract.image_to_data(img)
for x, box in enumerate(boxes.splitlines()):
    if x != 0:
        box = box.split()
        print(box)
        if len(box) == 12:
            x, y, w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
            cv2.rectangle(img, (x, y), (w + x, h + y), (0, 255, 0), 2)
            cv2.putText(img, box[11], (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)

if "Output" not in os.listdir():
    os.mkdir("Output")
os.chdir("Output")

cv2.imwrite("WordDetection.png", img)
cv2.imshow("Image", img)
cv2.waitKey(0)

