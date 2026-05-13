from PIL import Image
import numpy as np

# Load image
img = Image.open("image.jpg")

# Convert to array
img_array = np.array(img)

# Print details
print("Image Shape:", img_array.shape)
print("Pixel Values (first 5 pixels):")
print(img_array[0][0:5])
print("Number of Channels:", img_array.shape[2])