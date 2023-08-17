from skimage import io, transform

# Carregando imagem
image = io.imread(r"imgs\004_messi.jpg")

# Rotacionando imagem
rotate = transform.rotate(image, 45)

# Mostrando resultado
io.imshow(rotate)
io.show()
