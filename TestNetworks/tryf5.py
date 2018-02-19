import gzip
import io
import base64
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import tostring

def gzip_str(string_):
    out = io.BytesIO()

    with gzip.GzipFile(fileobj=out, mode='w') as fo:
        fo.write(string_.encode('ascii'))

    bytes_obj = out.getvalue()
    return bytes_obj

def gunzip_bytes_obj(bytes_obj):
    in_ = io.BytesIO()
    in_.write(bytes_obj)
    in_.seek(0)
    with gzip.GzipFile(fileobj=in_, mode='rb') as fo:
        gunzipped_bytes_obj = fo.read()
    return gunzipped_bytes_obj.decode('ascii')

image = open('Training4.xml', 'wb')
#image_read = image.read()
ET = ElementTree()
tree = ET.parse('Training.xml')
isFlag = False
attr = input()
for trac in tree.iter():
    if attr.split('=')[0] in trac.attrib:
        print("yes")
        for book in tree.findall('.//*[@test="1"]'):

            for elem in book.iter():
                if isFlag:
                    s2 = gzip_str(elem.text)
                    s3 = gzip_str(elem.tag)
                    try:
                        elem.text = elem.text.replace(elem.text, str(s2)[1:])
                        #elem.tag = elem.tag.replace(elem.tag, str(s3)[1:])
                    except AttributeError:
                        pass
                    #print(elem.text)
                    print(gunzip_bytes_obj(s2))
                    ElementTree(elem).write(image)

                isFlag = True
        break
    else:
        ElementTree(trac).write(image)
     # for elem in book.iter():
     #     #book.set(base64.b64encode(elem.text.encode('ascii')))
     #     if isFlag:
    #s2 = base64.b64encode(elem.text.encode('ascii'))
    #print(str(s2)[1:])


    #print(elem.text)

     #        # print(s2)
     #        # print(base64.b64decode(s2).decode('ascii'))
     #        ElementTree(elem).write(image,encoding='utf-8',method="xml")
     #        #ElementTree(elem).write(image)
     #     isFlag = True
         #print(base64.b64decode(s2).decode('ascii'))
         #image_64_encode = base64.b64encode(elem.text)


