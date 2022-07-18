#!/usr/bin/python3

def list_division(list_1, list_2, list_len):
    result = []
    for i in range(list_len):
        try:
            quotient = list_1[i] / list_2[i]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            result.append(quotient if quotient else 0)
            quotient = None

    return result


if __name__ == "__main__":
    list_division()
