from skimage import io, filters, color, morphology
from matplotlib import pyplot as plt

img = io.imread(r"imgs\img014.jpg")
gray_img = color.rgb2gray(img)

th = filters.threshold_otsu(gray_img)
binary_img = gray_img > th

# opened
opened_img = morphology.opening(binary_img, morphology.square(3))

# closed
closed_img = morphology.closing(binary_img, morphology.square(3))

# View the resulting images
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].imshow(opened_img, cmap='gray')
axes[0].axis('off')
axes[0].set_title('Opening')
axes[1].imshow(closed_img, cmap='gray')
axes[1].axis('off')
axes[1].set_title('Closing')
plt.show()
