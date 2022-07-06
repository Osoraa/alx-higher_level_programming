#!/usr/bin/python3


def best_score(a_dict={}):
    if not a_dict:
        return None

    # Create a 2D list to hold dict key-value pair.
    # Sort 2D list to find largest dict_value and then return associated key
    dict_list = [[key, value] for key, value in a_dict.items()]
    dict_list.sort(key=lambda x: x[1], reverse=True)

    return dict_list[0][0]


if __name__ == "__main__":
    best_score()
