from PIL import Image

img = Image.open("myface1.jpg")
area = (100,100,150,150)
cropped_img = img.crop(area)
img.show()
cropped_img.show()
