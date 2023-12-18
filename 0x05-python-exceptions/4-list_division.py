#!/usr/bin/python3
""" A function that divides element by element 2 lists."""


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(0, list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            res = my_list_1[i] / my_list_2[i]
            if not isinstance(res, (int, float)):
                raise TypeError("wrong type")
            result.append(res)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return (result)
