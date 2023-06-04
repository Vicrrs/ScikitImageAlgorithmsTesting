from skimage import io, filters, color
from matplotlib import pyplot as plt

img = io.imread(r"imgs\img014.jpg")
gray_img = color.rgb2gray(img)
threshold = filters.threshold_otsu(gray_img)
binary_img = gray_img > threshold

blurred_img = filters.gaussian(gray_img, sigma=2)

# blur filter
plt.imshow(blurred_img, cmap='gray')
plt.show()
