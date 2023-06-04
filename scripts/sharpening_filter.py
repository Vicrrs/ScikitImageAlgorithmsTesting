import skimage
from skimage import io
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt


image = io.imread(r'imgs\img05.jpg')


gray_image = skimage.color.rgb2gray(image)

# applying sharpening filter
sharpened_image = gray_image + 2 * \
    (gray_image - gaussian_filter(gray_image, sigma=1))

# show img
plt.imshow(sharpened_image, cmap='gray')
plt.axis('off')
plt.show()
