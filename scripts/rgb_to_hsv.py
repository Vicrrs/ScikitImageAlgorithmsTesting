import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2hsv

img = io.imread(r"C:\Users\rozas\Documents\Projects\ScikitImageAlgorithmsTesting\imgs\messi.jpg")

hsv_img = rgb2hsv(img)
hue_img = hsv_img[:, :, 0]
value_img = hsv_img[:, :, 2]

fig, (ax0, ax1, ax2) = plt.subplots(ncols=3, figsize=(8, 2))

ax0.imshow(img)
ax0.set_title("RGB image")
ax0.axis('off')
ax1.imshow(hue_img, cmap='hsv')
ax1.set_title("Hue channel")
ax1.axis('off')
ax2.imshow(value_img)
ax2.set_title("Value channel")
ax2.axis('off')

fig.tight_layout()
plt.show()
