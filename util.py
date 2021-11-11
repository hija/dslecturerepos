import requests
from PIL import Image
from io import BytesIO
import numpy as np


headers = {
    'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}


def load_image_bytes(url):
    return requests.get(url, headers=headers).content


def content_to_ndarray(im_bytes):
    bytes_io = bytearray(im_bytes)
    img = Image.open(BytesIO(bytes_io))
    return np.array(img)


def load_image_from_url(url):
    return content_to_ndarray(load_image_bytes(url))

def load_images():
    filenames = [f'https://mci-datascience.at/datasets/example{i}.jpg' for i in range(1,7)]
    images = list(map(load_image_from_url, filenames))
    return images