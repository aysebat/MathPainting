import numpy as np
from PIL import Image
class Canvas:
    """Description: Object where all shapes are going to drawn"""

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Creates a 3d numpy array of zeros
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        # change [0,0,0] with user given color
        self.data[:] = self.color

    def make(self, imagepath):
        image = Image.fromarray(self.data, 'RGB')
        image.save(imagepath)
