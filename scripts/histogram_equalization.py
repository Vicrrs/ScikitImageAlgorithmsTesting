from skimage import io, filters, color, exposure
from matplotlib import pyplot as plt

img = io.imread(r"imgs\img01.jpeg")
gray_img = color.rgb2gray(img)
threshold = filters.threshold_otsu(gray_img)
binary_img = gray_img > threshold

# Equalização de histograma
equalized_image = exposure.equalize_hist(gray_img)

# Exibir a imagem equalizada
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')
plt.show()
