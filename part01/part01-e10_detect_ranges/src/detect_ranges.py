#!/usr/bin/env python3

def detect_ranges(L: list) -> list:
    sorted_list: list[int] = sorted(L)

    diff: list[int] = []
    for i in range(len(sorted_list)-1):
        diff.append(sorted_list[i+1] - sorted_list[i])
    diff.insert(0, 0)

    ind: list[int] = []
    for i in range(len(diff)):
        if diff[i] >= 2:
            ind.append(i)
    ind.insert(0, 0)

    groups: list[int] = []
    for i in range(len(ind)):
        if i == len(ind)-1:
            groups.append(sorted_list[ind[i]:])
        else:
            groups.append(sorted_list[ind[i]:ind[i+1]])

    desired_list: list[int] = []
    for group in groups:
        if len(group) >= 2:
            desired_list.append((group[0], group[len(group)-1] + 1))
        else:
            desired_list.append(group[0])

    return desired_list


def main() -> None:
    L: list[int] = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result: list[int] = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
