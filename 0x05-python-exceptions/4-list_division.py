#!/usr/bin/python3

def list_division(list_1, list_2, list_len):
    result = []
    for i in range(list_len):
        try:
            quotient = list_1[i] / list_2[i]
        except IndexError:
            print("out of range")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except TypeError:
            print("wrong type")
            quotient = 0
        finally:
            result.append(quotient)

    return result


if __name__ == "__main__":
    list_division()
