#!/usr/bin/env python3

def distinct_characters(L: list) -> dict:
    return {word: len(set(word)) for word in L}


def main() -> None:
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()
