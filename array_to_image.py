import numpy as np
from PIL import Image

#Create a numpy array zeros
data = np.zeros([5,4,3], dtype=np.uint8)
#replace the zeros with yellow color
data[:] = [255, 255, 0]
#print(data)
#first row, second column
#Create red  takes all column and row from 1 t0 3
data[:, 1:3] = [255, 0, 0]

#Create blue shape takes column 1 to 2 and all roe
data[1:2,:] = [0,0,255]

#create  green shape takes last one column(4:5) and last row(3:4)
data[4:5, 3:4] = [0,255,0]

img = Image.fromarray(data, 'RGB')

img.save('canvas.png')
print('Saved images')
