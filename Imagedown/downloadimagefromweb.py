import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://thenewboston.com/images/forum/logos/dfdfdb6ea30dd264d092183442b4ec5c.png")
