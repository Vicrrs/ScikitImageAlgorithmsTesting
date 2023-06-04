from skimage import io, filters, color, morphology
from matplotlib import pyplot as plt

img = io.imread(r"imgs\img014.jpg")
gray_img = color.rgb2gray(img)

th = filters.threshold_otsu(gray_img)
binary_img = gray_img > th

# Erosion
erode_img = morphology.erosion(binary_img, morphology.square(3))

# dilate
dilated_img = morphology.dilation(binary_img, morphology.square(3))

# View the resulting images
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].imshow(erode_img, cmap='gray')
axes[0].axis('off')
axes[0].set_title('Erosion')
axes[1].imshow(dilated_img, cmap='gray')
axes[1].axis('off')
axes[1].set_title('Dilation')
plt.show()
