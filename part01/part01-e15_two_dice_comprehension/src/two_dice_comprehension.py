#!/usr/bin/env python3

def main():
    """Solution given by tmc.mooc.fi course staff."""
    print("\n".join(f"({i}, {j})"
                    for i in range(1, 6)
                    for j in range(1, 6)
                    if i+j == 5))


if __name__ == "__main__":
    main()


# My attempt
#
# def main():
#     des_lst = [(i, j)
#                for i in range(1, 6)
#                for j in range(1, 6)
#                if i+j == 5]
#     for item in des_lst:
#         print(item)
