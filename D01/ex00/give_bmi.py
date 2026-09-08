import numpy as np


def check_list(list_to_check: list[int | float]):
    """check list specifications"""
    if list_to_check is None or len(list_to_check) == 0:
        raise ValueError("The list should not be none or empty.")
    if not isinstance(list_to_check, list):
        raise TypeError("The params passsed should be a list")
    if not all(isinstance(item, (int, float)) for item in list_to_check):
        raise TypeError("The list should contain only int or float.")


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """Calculate a list of bmi using hight/wight params"""
    check_list(height)
    check_list(weight)
    if len(weight) != len(height):
        raise ValueError("The lists should be same size")
    if any(item <= 0 for item in height):
        raise ValueError("The value of height should be postive and not zero.")
    if any(item < 0 for item in weight):
        raise ValueError("The value of weight should not be negative")
    height_array = np.array(height)
    weight_array = np.array(weight)
    bmi_result = weight_array / height_array ** 2
    return bmi_result.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit on bmi list and return a list of bools"""
    check_list(bmi)
    if not isinstance(limit, int):
        raise TypeError("The limit should be an integer.")
    nd_bmi = np.array(bmi)
    results = nd_bmi > limit
    return results.tolist()


def main():
    """The main to test the give_bmi and apply_limit on bmi"""
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
