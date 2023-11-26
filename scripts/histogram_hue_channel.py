import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2hsv

img = io.imread(r"C:\Users\rozas\Documents\Projects\ScikitImageAlgorithmsTesting\imgs\messi.jpg")

hsv_img = rgb2hsv(img)
hue_img = hsv_img[:, :, 0]
value_img = hsv_img[:, :, 2]

hue_threshold = 0.04
binary_img = hue_img > hue_threshold

fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 3))

ax0.hist(hue_img.ravel(), 512)
ax0.set_title("Histogram of the Hue channel with threshold")
ax0.axvline(x=hue_threshold, color='r', linestyle='dashed', linewidth=2)
ax0.set_xbound(0, 0.12)
ax1.imshow(binary_img)
ax1.set_title("Hue-thresholded image")
ax1.axis('off')

fig.tight_layout()
plt.show()
