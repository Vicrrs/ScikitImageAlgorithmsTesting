import os
import skimage
from skimage import io
from matplotlib import pyplot as plt

file_name = os.path.join(
    skimage.data_dir,
    r"C:\Users\rozas\Projects\ScikitImageAlgorithmsTesting\imgs\img04.png")
lena = io.imread(file_name)

plt.imshow(lena)
plt.show()
