from numpy import array
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def ft_load(path: str) -> array:
    try:
        import matplotlib
        print(matplotlib.__version__)
        import sys
        print("Running with Python version:", sys.version)

        img = Image.open(path, 'r')
        data = np.array(img)
        print(f"The shape of image is: {data.shape}")
        plt.xlabel("X axis (width in pixels)")
        plt.ylabel("Y axis (height in pixels)")
        plt.title("Image with X and Y Scale")
        plt.grid(False)  # Optional: turn off grid
        plt.imshow(data)
        plt.show()
        # return data

    except Exception as e:
        print(f"an error ocuured {e}")
        return []


    



