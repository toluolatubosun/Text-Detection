import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('Text.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Image To String
text = pytesseract.image_to_string(img)
print(text)
with open("Output/ImageToText.txt", "w") as f:
    f.write(text)
    f.close()

cv2.imshow("Image", img)
cv2.waitKey(0)

