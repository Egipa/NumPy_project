import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time


def resize_image(img_path, new_size):
    # Open and resize image
    img = Image.open(img_path)
    img_array = np.array(img)
    resize_img = np.array(Image.fromarray(img_array).resize(new_size))
    Image.fromarray(resize_img).save('resized_image.jpg')
    return resize_img


def split_image(img_array, num_slices, axis):
    # Split image into parts along given axis
    img_parts = np.split(img_array, num_slices, axis=axis)
    return img_parts


def concatenate_image_parts(img_parts, indices, axis):
    # Concatenate image parts given a list of indices
    concat_img = np.concatenate(img_parts[indices[0]::indices[1]], axis=axis)
    return concat_img


start_time = time.time()
# Resize the image to be able to split into fixed number of slices
new_size = (1600, 1000)
resize_img = resize_image('jaguar_profile.jpg', new_size)
# resize_img = resize_image('car_profile.jpg', new_size)

resize_time = time.time()
print(f'Resizing time: {resize_time - start_time:.2f}s')

# Split the image into vertical parts
img_parts_vertical = split_image(resize_img, 160, axis=1)

# Concatenate every second image part vertically
concat_img_vertical1 = concatenate_image_parts(img_parts_vertical, [0,2], axis=1)
concat_img_vertical2 = concatenate_image_parts(img_parts_vertical, [1,2], axis=1)
vertical_concat = np.concatenate((concat_img_vertical1, concat_img_vertical2), axis=1)

split_time = time.time()
print(f'Splitting time: {split_time - resize_time:.2f}s')

concat_time = time.time()

# Split the image into horizontal parts
img_parts_horizontal = split_image(vertical_concat, 100, axis=0)

# Concatenate every second image part horizontally
concat_img_horizontal1 = concatenate_image_parts(img_parts_horizontal, [0,2], axis=0)
concat_img_horizontal2 = concatenate_image_parts(img_parts_horizontal, [1,2], axis=0)
horizontal_concat = np.concatenate((concat_img_horizontal1, concat_img_horizontal2), axis=1)
end_time = time.time()
print(f'Concatenation time: {end_time - concat_time:.2f}s')

# Display intermedia result of the image
plt.imshow(vertical_concat)
plt.show()

# Display the concatenated image
plt.imshow(horizontal_concat)
plt.show()
