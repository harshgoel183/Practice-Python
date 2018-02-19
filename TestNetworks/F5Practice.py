import os, time, gzip
import base64
import xml.etree.ElementTree as ET
from xml.etree.cElementTree import ElementTree
tree = ET.parse('Training.xml')

#attr = input()
isFlag = False
for book in tree.findall('.//*[@test="1"]'):
    #ElementTree(book).write('Training4.xml')
    for elem in book.iter():
        print(elem.tag,elem.text)
        print(base64.b64encode(elem.text.encode('ascii')))
        #if isFlag:
            #print()
        #ElementTree(elem).write('Training4.xml')
             #print(elem.tag,elem.text)
             #print(base64.b64encode(elem.text.encode('ascii')))
             #print(base64.b64encode(elem.tag.encode('ascii')))
            # elem.text = base64.b64encode(elem.text.encode('utf-8'))
            # #elem.tag = base64.b64encode(elem.tag.encode('utf-8'))
            # ElementTree(elem).write('Training4.xml')
            # #elem.tag.write('Training4.xml')
        #isFlag = True
