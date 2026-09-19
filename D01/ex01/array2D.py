import numpy as np


def check_2D_array(family: list):
    """this function is to check if the array is 2D valide array"""
    if family is None or len(family) == 0:
        raise ValueError("The list should not be none or empty")
    if not all(isinstance(item, list) for item in family):
        raise TypeError("All rows should be a list, so this is not a 2D array")
    if any(isinstance(item, list) for row in family for item in row):
        raise TypeError("The array is not a 2D array")


def slice_me(family: list, start: int, end: int) -> list:
    """a fucntion to slice a 2D starting from start to end and return a list"""
    check_2D_array(family)
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("the start and end index should be int")
    array_family = np.array(family)
    print(f"My shape is : {array_family.shape}")
    array_family = array_family[start: end]
    print(f"My new shape is : {array_family.shape}")
    return array_family.tolist()


def main():
    """Main to test the function slice_me"""
    family = [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
            ]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
