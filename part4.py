import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('Text.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Digit Detection
hImg, wImg, layer = img.shape
config = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img, config=config)
for box in boxes.splitlines():
    box = box.split(' ')
    # print(box)
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 255, 0), 2)
    cv2.putText(img, box[0], (x, hImg - y + 20), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)

if "Output" not in os.listdir():
    os.mkdir("Output")
os.chdir("Output")

cv2.imwrite("DigitDetection.png", img)
cv2.imshow("Image", img)
cv2.waitKey(0)


