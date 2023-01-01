import requests
from PIL import Image
from io import BytesIO


def get_image_size_url(url):
    data = requests.get(url).content
    im = Image.open(BytesIO(data))    
    return im.size

if __name__ == "__main__":
    url = "https://codigoespagueti.com/wp-content/uploads/2022/11/dragon-ball-super.jpg"
    width, height = get_image_size_url(url)
    print(width, height)