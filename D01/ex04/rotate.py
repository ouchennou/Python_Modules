from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_rotate(img: np.ndarray) -> np.ndarray:
    """rotate the image"""
    if not isinstance(img, np.ndarray):
        raise TypeError("The array is not a nd array")
    if img.ndim != 2 or img.size == 0:
        raise ValueError("the array should be 2d and not empty")
    result = []
    row_index = len(img)
    for index in range(row_index):
        new_row = []
        for col_index in range(len(img[index])):
            new_row.append(img[col_index][index])
        result.append(new_row)
    return np.array(result)


def main():
    """Load image and rotate it"""
    try:
        img_array = ft_load("../animal.jpeg")
        square_img = img_array[200:600, 300:700, 0:1]
        print(f"The shape of image is: {square_img.shape} or \
              {square_img[:, :, 0].shape}")
        print(square_img)
        img_rotated = ft_rotate(square_img[:, :, 0])
        print(f"New shape after trasnpose: {img_rotated.shape}")
        print(img_rotated)
        plt.imshow(img_rotated, cmap="gray")
        plt.show()
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
