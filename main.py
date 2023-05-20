import pywhatkit as kit
import cv2

kit.text_to_handwriting("HI", save_to="handwriting.png", rgb=(0, 0, 0))
img = cv2.imread("handwriting.png")
print(img)

if img is not None:
    cv2.imshow("Text to Handwriting", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to load the image.")
