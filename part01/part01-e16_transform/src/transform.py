#!/usr/bin/env python3

def transform(s1, s2):
    """Take two strings and create integer lists, and return a list
    whose elements are the respective indices in the integer lists
    multiplied.
    """
    if s1 == "" or s2 == "":
        return []
    L1 = list(map(int, s1.split(" ")))
    L2 = list(map(int, s2.split(" ")))
    return [i*j for i, j in zip(L1, L2)]


def main():
    print(transform("1 5 3", "2 6 -1"))


if __name__ == "__main__":
    main()
