import requests
import gzip
import io
from xml.etree.ElementTree import ElementTree

def gzip_str(string_):
    out = io.BytesIO()

    with gzip.GzipFile(fileobj=out, mode='w') as fo:
         fo.write(string_.encode('utf-8'))

    bytes_obj = out.getvalue()
    return bytes_obj

def gunzip_bytes_obj(bytes_obj):
    in_ = io.BytesIO()
    in_.write(bytes_obj)
    in_.seek(0)
    with gzip.GzipFile(fileobj=in_, mode='rb') as fo:
        gunzipped_bytes_obj = fo.read()
    return gunzipped_bytes_obj.decode('utf-8')
text = []
tag = []
ET = ElementTree()
tree = ET.parse('Training.xml')
isFlag = False
print(r'Enter the attribute you want to select: Example-> test="1"')

attr = input()
print(r'Elements selected for encoding and zipping\n')
count=0
count1=0

for book in tree.findall('.//*[@'+attr+']'):
    isFlag = False
    for elem in book.iter():
        if isFlag:
            print(elem.text,elem.tag)
            s2 = gzip_str(elem.text)
            text.append(s2)

            s3 = gzip_str(elem.tag)
            tag.append(s3)
            try:
                elem.text = elem.text.replace(elem.text, str(s2)[1:])
                elem.tag = elem.tag.replace(elem.tag, str(s3)[1:])
            except AttributeError:
                pass

        else:
            print(elem.text)
            s2 = gzip_str(elem.text)
            text.append(s2)
            elem.text = elem.text.replace(elem.text, str(s2)[1:])
        isFlag = True
print('\n'r'Type gzip to compress the selected elements of the given attribute '+attr)
commandLine = input()
image = open('Training2.xml', 'wb')
if commandLine.startswith('gzip'):
    ElementTree(tree).write(image)
image.close()
print(r'xml file has been gzipped. gzipped file created Training2.xml')

print(r'The resulted file will be send to requested URL http://posttestserver.com/post.php'+'\n')

r = requests.post('http://posttestserver.com/post.php', files={'Training2.xml': open('Training2.xml', 'rb')})
print(r.text)
print('\n'+r'Type gunzip to retrieve the original xml file')
commandLine = input()
if commandLine.startswith('gunzip'):
    image1 = open('Training2.xml', 'wb')
for book in tree.findall('.//*[@'+attr+']'):
    isFlag = False
    for elem in book.iter():
        if isFlag:
            s2 = gunzip_bytes_obj(text[count])
            s3 = gunzip_bytes_obj(tag[count1])
            try:
                elem.text = elem.text.replace(elem.text, s2)
                elem.tag = elem.tag.replace(elem.tag, s3)
            except AttributeError:
                pass
            count += 1
            count1 += 1
        else:
            s2 = gunzip_bytes_obj(text[count])
            elem.text = elem.text.replace(elem.text, s2)
            count += 1
        isFlag = True

ElementTree(tree).write(image1)
image1.close()
