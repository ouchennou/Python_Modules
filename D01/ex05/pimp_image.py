import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_invert(img: np.ndarray) -> np.ndarray:
    """Invert the colors of image"""
    inverted_image = 255 - img
    plt.imshow(inverted_image)
    plt.show()
    return inverted_image


def ft_red(img: np.ndarray) -> np.ndarray:
    """make the image red"""
    red_image = img * [1, 0, 0]
    plt.imshow(red_image)
    plt.show()
    return red_image


def ft_green(img: np.ndarray) -> np.ndarray:
    """Make the image green color based"""
    green_img = img.copy()
    green_img[:, :, 0] = green_img[:, :, 0] - green_img[:, :, 0]
    green_img[:, :, 2] = green_img[:, :, 2] - green_img[:, :, 2]
    plt.imshow(green_img)
    plt.show()
    return green_img


def ft_blue(img: np.ndarray) -> np.ndarray:
    """Make the image based on blue"""
    blue_image = img.copy()
    blue_image[:, :, 0] = 0
    blue_image[:, :, 1] = 0
    plt.imshow(blue_image)
    plt.show()
    return blue_image


def ft_grey(img: np.ndarray) -> np.ndarray:
    """Make the image grey"""
    rgb_grey = np.sum(img, axis=2, keepdims=True) / 3
    grey_img = np.repeat(rgb_grey, 3, axis=2).astype(img.dtype)
    plt.imshow(grey_img)
    plt.show()
    return grey_img


def main():
    """Test the diffrence function to manipulate the images"""
    try:
        img = ft_load("../landscape.jpg")
        print(img.ndim)
        ft_invert(img)
        ft_green(img)
        ft_red(img)
        ft_blue(img)
        ft_grey(img)
        print(ft_invert.__doc__)
    except Exception as ex:
        print(f"Error : {ex}")


if __name__ == "__main__":
    main()
