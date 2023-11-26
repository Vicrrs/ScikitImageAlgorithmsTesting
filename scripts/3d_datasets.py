from skimage import data
import plotly
import plotly.express as px
import numpy as np

img = data.cells3d()[20:]

# omit some slices that are partially empty
img = img[5:26]

upper_limit = 1.5 * np.percentile(img, q=99)
img = np.clip(img, 0, upper_limit)

fig = px.imshow(
    img,
    facet_col=1,
    animation_frame=0,
    binary_string=True,
    binary_format="jpg",
)
fig.layout.annotations[0]["text"] = "Cell membranes"
fig.layout.annotations[1]["text"] = "Nuclei"
plotly.io.show(fig)