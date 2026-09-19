from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """Load anime image and zoom it"""
    try:
        img_array = ft_load("../animal.jpeg")
        print(img_array)
        zoomed_image = img_array[200:600, 400:800, 0:1]
        print(f"New shape after slicing: {zoomed_image.shape} or \
              {zoomed_image[:,:,0].shape}")
        print(zoomed_image)
        plt.imshow(zoomed_image[:, :, 0], cmap="gray")
        plt.show()
    except Exception as error:
        print(f"Error : {error}")


if __name__ == "__main__":
    main()
