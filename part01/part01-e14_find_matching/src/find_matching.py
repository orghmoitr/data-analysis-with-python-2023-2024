#!/usr/bin/env python3

def find_matching(L, pattern):
    """Take a list of strings and a pattern, and return a new list
    whose elements are the indices of the list where the pattern is
    in the string.
    """
    return [i for i, string in enumerate(L) if pattern in string]


def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))


if __name__ == "__main__":
    main()
