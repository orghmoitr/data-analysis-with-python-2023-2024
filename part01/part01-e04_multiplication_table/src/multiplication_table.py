#!/usr/bin/env python3

def main() -> None:
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{j * i:5d}", end="")
        print()


if __name__ == "__main__":
    main()
