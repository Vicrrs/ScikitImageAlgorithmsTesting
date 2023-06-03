from skimage import io, color
from matplotlib import pyplot as plt

img = io.imread(r"imgs\img014.jpg")
# Convert to grayscale
gray_img = color.rgb2gray(img)

plt.imshow(gray_img, cmap="gray")
plt.show()
