#!/usr/bin/env python3

def sum_equation(L):
    """Take a list and return a string with an equation of the
    sum of the elements in the list.
    """
    if not L:
        return "0 = 0"
    des_lst = list(map(str, L))
    return " + ".join(des_lst) + " = " + f"{sum(L)}"


def main():
    print(sum_equation([1, 5, 7]))


if __name__ == "__main__":
    main()


# My attempt
#
# from functools import reduce
#
#
# def sum_equation(L):
#     """Take a list and return a string with an equation of the
#     sum of the elements in the list.
#     """
#     if not L:
#         return "0 = 0"
#     sum_of_elements = reduce(lambda total, number: total + number, L, 0)
#     result = ""
#     for i in range(len(L)):
#         if i == len(L)-1:
#             result += f"{L[i]} = {sum_of_elements}"
#         else:
#             result += f"{L[i]} + "
#     return result
