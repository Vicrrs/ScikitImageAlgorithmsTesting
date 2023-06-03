import os
import skimage
from skimage import io
from skimage import filters
from matplotlib import pyplot as plt

# caminho pra imagem
img_path = os.path.join(
    skimage.data_dir,
    r"C:\Users\rozas\Projects\ScikitImageAlgorithmsTesting\imgs\img014.jpg")

# carregando imagem em escala de cinza
img = io.imread(img_path, as_gray=True)

# aplicando limiar otsu
th = filters.threshold_otsu(img)

# segmentando a imagem com base no limiar
binary_img = img > th

# mostrando imagem binaria
plt.imshow(binary_img, cmap="gray")
plt.show()
