from PIL import Image

img = Image.open("myface1.jpg")
img2 = Image.open("bullet.png")

area = (50,50,74,74)
img.paste(img2, area)
img.show()
