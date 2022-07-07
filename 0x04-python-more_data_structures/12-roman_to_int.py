#!/usr/bin/python3


def roman_to_int(roman_str) -> int:
    r_nums = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    r_list = list(roman_str)[::-1]
    result = r_nums[r_list[0]]

    for i in range(1, len(r_list)):
        if r_nums[r_list[i]] < r_nums[r_list[i-1]]:
            result -= r_nums[r_list[i]]
        else:
            result += r_nums[r_list[i]]

    return result


if __name__ == "__main__":
    roman_to_int()
