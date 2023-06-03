from skimage import io
from matplotlib import pyplot as plt

# loading image
img = io.imread(r"imgs\img02.png")

# displaying the image
plt.imshow(img)
plt.show()
