from PIL import Image, ImageFilter

img = Image.open('e:/1.jpg')
w, h = img.size
print(w, h)
# img2=img.filter(ImageFilter.BLUR)
img.thumbnail((2000 * w / h, 2000))
img.save('e:/copy1.jpg')
# img.load()
# img.show()
