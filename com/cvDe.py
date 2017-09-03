from PIL import Image
import pytesseract

# img = Image.open('e:/hello.png')
# img.load()
# img.show()
print(pytesseract.image_to_string(Image.open('e:/en.png'), lang='eng'))
