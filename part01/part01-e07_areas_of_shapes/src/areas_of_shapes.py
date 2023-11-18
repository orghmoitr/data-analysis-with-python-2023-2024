#!/usr/bin/env python3

import math


def area_of_triangle() -> float:
    base: int = int(input("Give base of the triangle: "))
    height: int = int(input("Give height of the triangle: "))
    return (base*height) / 2


def area_of_rectangle() -> int:
    width: int = int(input("Give width of the rectangle: "))
    height: int = int(input("Give height of the rectangle: "))
    return width * height


def area_of_circle() -> float:
    radius: int = int(input("Give radius of the circle: "))
    return math.pi * radius * radius


def main() -> None:
    while True:
        user_input: str = input("Choose a shape (triangle, rectangle, circle): ")
        if user_input == "":
            break
        elif user_input == "triangle":
            print(f"The area is {area_of_triangle():6f}")
        elif user_input == "rectangle":
            print(f"The area is {area_of_rectangle():6f}")
        elif user_input == "circle":
            print(f"The area is {area_of_circle():6f}")
        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
