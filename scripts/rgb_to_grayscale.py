import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import io

img = io.imread(r"C:\Users\rozas\Documents\Projects\ScikitImageAlgorithmsTesting\imgs\messi.jpg")
grayscale = rgb2gray(img)

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax = axes.ravel()

ax[0].imshow(img)
ax[0].set_title("Original")
ax[1].imshow(grayscale, cmap=plt.cm.gray)
ax[1].set_title("Grayscale")

fig.tight_layout()
plt.show()
