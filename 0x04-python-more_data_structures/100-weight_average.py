#!/usr/bin/python3


def weight_average(my_list=[]) -> float:
    if not my_list:
        return 0

    product = sum([num[0] * num[1] for num in my_list])
    total_count = sum([num[1] for num in my_list])

    return product / total_count


if __name__ == "__main__":
    weight_average()
