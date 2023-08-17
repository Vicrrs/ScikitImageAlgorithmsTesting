from skimage import io, color, transform, filters
import numpy as np

image = io.imread(r"imgs\007_estrada.jpg")
gray_image = color.rgb2gray(image)
edges = filters.sobel(gray_image)
hough, theta, rho = transform.hough_line(edges)
io.imshow(np.log(1 + hough), extent=[0, np.rad2deg(theta[-1]), -rho.max(), rho.max()], cmap='gray', aspect=1/1.5)
io.show()
