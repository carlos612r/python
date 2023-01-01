import requests
from PIL import Image
from io import BytesIO

class Photo:
    def __init__(self, url):
        self.data = requests.get(url).content
         
    def get_image_size_url(self):
        image = Image.open(BytesIO(self.data))    
        return image.size

image = Photo("https://codigoespagueti.com/wp-content/uploads/2022/11/dragon-ball-super.jpg")
reponse = image.get_image_size_url()
print(reponse)