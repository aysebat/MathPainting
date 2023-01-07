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
        image = Image.fromaaray(self.data, 'RGB')
        image.save(imagepath)


class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """Draw itself into canvas
           Change a slice of the array with new value"""
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        """Draw itself into canvas
        Change a slice of the array with new value"""
        canvas.data[self.x:self.x + self.width, self.y: self.y + self.height] = self.color
