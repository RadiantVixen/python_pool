from numpy import array
from PIL import Image
import numpy as np

def ft_load(path: str) -> array:
    try:
        img = Image.open(path, 'r')
        data = np.array(img)
        print(f"The shape of image is: {data.shape}")
        return data
    except Exception as e:
        print(f"an error ocuured {e}")
        return []


    



