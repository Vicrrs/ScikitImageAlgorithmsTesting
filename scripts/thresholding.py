from skimage import io, filters, color
from matplotlib import pyplot as plt

img = io.imread(r"imgs\img014.jpg")
gray_img = color.rgb2gray(img)

# Aplicar limiar de Otsu
th = filters.threshold_otsu(gray_img)
binary_img = gray_img > th

# Exibir a imagem binarizada
plt.imshow(binary_img, cmap='gray')
plt.show()
