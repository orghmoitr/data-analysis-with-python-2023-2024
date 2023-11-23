#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle


def main():
    print(triangle.hypotenuse(20, 5))
    print(triangle.area(4, 34))

    print(triangle.__version__)
    print(triangle.__author__)


if __name__ == "__main__":
    main()
