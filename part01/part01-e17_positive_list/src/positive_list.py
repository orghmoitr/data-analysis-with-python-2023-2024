#!/usr/bin/env python3

def positive_list(L):
    """Take a list and return a list that filters out
    negative numbers and zero.
    """
    return [n for n in list(filter(lambda x: x > 0, L))]


def main():
    print(positive_list([2, -2, 0, 1, -7]))


if __name__ == "__main__":
    main()
