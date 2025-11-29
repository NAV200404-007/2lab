
def display_main_menu():
    print("display_main_menu")

def get_user_input():
    print("get_user_input")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32):")
    # 1. Read input
    x = input()
    # 2. Split by comma
    split = x.split(",")
    # 3. Convert to list of floats
    float_split = [float(i) for i in split]
    # 4. Return list of floats
    return float_split


def calc_average(temp):
    print("calc_average")
    avg = sum(temp) / len(temp)
    return avg

def find_min_max(temp):
    print("find_min_max")
    minimum = min(temp)
    maximum = max(temp)
    return minimum, maximum


def sort_temperature(temp):
    print("sort_temperature")
    sorted_split = sorted(temp)
    return sorted_split


def calc_median_temperature(temp):
    print("calc_median_temperature")
    temp = sorted(temp)
    n = len(temp)

    if n % 2 == 1:  # odd count
        return temp[n // 2]
    else:  # even count
        return (temp[n // 2 - 1] + temp[n // 2]) / 2
    


