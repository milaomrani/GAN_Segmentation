import matplotlib.pyplot as plt
from skimage.io import imread
from skimage import color
import numpy as np

cimage = imread('.../TRainingImages/1.jpg')
fig, ax = plt.subplots(figsize=(20, 20))
ax.imshow(cimage)
ax.axis('off')

# convert the image from RGB to LAB
lab_img = color.rgb2lab(cimage)
x, y, z = lab_img.shape

# to plot the colors we will use the RGB values from the
# image directly for colors. 
to_plot = cimage.reshape(x * y, 3)
colors_map = to_plot.astype(np.float) / 256

# create dataset for scatter plot
scatter_x = []
scatter_y = []
for xi in range(x):
    for yi in range(y):
        L_val = lab_img[xi, yi][0]
        A_val = lab_img[xi, yi][1]
        B_val = lab_img[xi, yi][2]
        scatter_x.append(A_val)
        scatter_y.append(B_val)

plt.figure(figsize=(20, 20))
plt.xlabel("a* from green to red")
plt.ylabel("b* from blue to yellow")
plt.scatter(scatter_x, scatter_y, c=colors_map)

plt.show()
