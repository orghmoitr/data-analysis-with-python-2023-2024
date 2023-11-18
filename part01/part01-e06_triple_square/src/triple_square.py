#!/usr/bin/env python3

def triple(n: int) -> int:
    return n * 3


def square(n: int) -> int:
    return n ** 2


def main() -> None:
    for i in range(1, 11):
        t: int = triple(i)
        s: int = square(i)
        if s > t:
            break
        print(f"triple({i})=={t} square({i})=={s}")


if __name__ == "__main__":
    main()
