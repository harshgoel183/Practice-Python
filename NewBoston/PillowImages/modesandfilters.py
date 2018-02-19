from PIL import Image
from PIL import ImageFilter

img = Image.open("myface1.jpg")
black_white = img.convert("L")
black_white.show()

blur = img.filter(ImageFilter.BLUR)
detail = img.filter(ImageFilter.DETAIL)
edges = img.filter(ImageFilter.FIND_EDGES)

blur.show()

edges.show()
detail.show()
img.show()
