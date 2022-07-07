#!/usr/bin/python3


def complex_delete(a_dict, del_value) -> dict:
    while del_value in a_dict.values():
        for key, value in a_dict.items():
            if value is del_value:
                del a_dict[key]
                break

    return a_dict


if __name__ == "__main__":
    complex_delete()
