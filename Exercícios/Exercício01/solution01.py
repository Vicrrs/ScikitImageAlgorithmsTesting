"""
Segmentação de Imagens com Watershed:

Objetivo: Implementar a segmentação de uma imagem complexa usando a técnica de watershed.
Desafio: Aplicar pré-processamento adequado para destacar fronteiras entre objetos.

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\rozas\Documents\Projects\ScikitImageAlgorithmsTesting\imgs\cells02.jpg")
assert img is not None, "Não foi possivel acessar imagem!"
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# remocao de ruido
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# area de fundo
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Area de primeiro plano correta
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
