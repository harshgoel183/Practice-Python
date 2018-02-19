from PIL import Image

img = Image.open("myface1.jpg")
img2 = Image.open("bullet.png")

r, g, b = img.split()
print(img.mode)
print(img2.mode)
r1, g1, b1, a = img2.split()

new_img = Image.merge("RGB", (r, g, b))
new_img2 = Image.merge("RGB", (b, g, r))
new_img3 = Image.merge("RGB", (g, r, b))

new_img4 = Image.merge("RGB", (g1, a, b1))
new_img.show()
new_img2.show()
new_img3.show()
new_img4.show()

