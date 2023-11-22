#!/usr/bin/env python3

def interleave(*lists: list) -> list:
    return [item for tup in zip(*lists) for item in tup]


def main() -> None:
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))


if __name__ == "__main__":
    main()
