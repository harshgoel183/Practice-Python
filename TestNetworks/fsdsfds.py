import base64
image = open('Training4.xml', 'rb')
image_read = image.read()
image_64_encode = base64.b64decode(image_read)
image_result = open('Training5.xml', 'wb') # create a writable image and write the decoding result
image_result.write(image_64_encode)
#print(image_64_decode)
