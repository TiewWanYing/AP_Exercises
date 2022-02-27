#import easyocr
#reader = easyocr.Reader(['jpn','en'], gpu=False)#this need to run only once to load #the model
#result = reader.readtext('RECEIPT.jpg')

import cv2
import pytesseract

def ocr_core(img):
	custom_config = r'-l jpn+en --psm 6'
	text = pytesseract.image_to_string(img, config=custom_config)
	return text

img = cv2.imread('RECEIPT.jpg')

#get grayscale image
def get_grayscale(image):
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#noise removal
def remove_noise(image):
	return cv2.medianBlur(image,5)

#thresholding
def thresholding(image):
	return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img = get_grayscale(img)
img = thresholding(img)
img = remove_noise(img)

print(ocr_core(img))

#cv2.imshow('img', img)
#cv2.waitKey(0)
