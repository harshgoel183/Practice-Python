from PIL import Image

img = Image.open("myface1.jpg")
square_img = img.resize((150, 150))
flip_img = img.transpose(Image.FLIP_TOP_BOTTOM)
spin_img = img.transpose(Image.ROTATE_90)

img.show()
square_img.show()
flip_img.show()
spin_img.show()
