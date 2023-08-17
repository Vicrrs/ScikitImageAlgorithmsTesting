from skimage import io, transform

# Carregando imagem
image = io.imread(r"imgs\014_placa-mercosul.png")

# Redimensionando imagem
resized = transform.resize(image, (100, 200))

# Mostrando resultado
io.imshow(resized)
io.show()
