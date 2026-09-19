import numpy as np
from PIL import Image as im


def check_path(path):
    """check the path file string is valid"""
    if not isinstance(path, str):
        raise TypeError("The path should be a pathing.")
    if path is None or not path:
        raise ValueError("The path should not be none or empty")
    if not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError("The image formats is not supported.")


def ft_load(path: str) -> np.ndarray:
    """Load image using the file path"""
    check_path(path)
    try:
        with im.open(path) as pic:
            rgb_pic = pic.convert("RGB")
            image_array = np.array(rgb_pic)
            print(f"The shape of image is: {image_array.shape}")
            return image_array
    except FileNotFoundError:
        raise FileNotFoundError(f"The filepath {path} doesn't exit.")
    except im.UnidentifiedImageError as error:
        raise ValueError(f"The image cannot be opened: {error}")
    except OSError as error:
        raise OSError(f"Cannot read the file {path}: {error}")


def main():
    """Test the ft_load function"""
    try:
        print(ft_load("../landscape.jpg"))
    except Exception as ex:
        print(f"Error: {ex}")


if __name__ == "__main__":
    main()
