#!/usr/bin/env python3

def merge_sort(merged: list, low: int, mid: int, high: int) -> list:
    i: int = low
    j: int = mid + 1
    aux: list[int] = []
    for item in merged:
        aux.append(item)
    for k in range(len(aux)):
        if i > mid:
            merged[k] = aux[j]
            j += 1
        elif j > high:
            merged[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            merged[k] = aux[j]
            j += 1
        else:
            merged[k] = aux[i]
            i += 1
    return merged


def merge(L1: list, L2: list) -> list:
    merged: list[int] = []
    for item in L1:
        merged.append(item)
    for item in L2:
        merged.append(item)
    low: int = 0
    mid: int = len(L1) - 1
    high: int = len(merged) - 1
    return merge_sort(merged, low, mid, high)


def main():
    L1: list[int] = [-96, -87, -84, -75, -72, -71, -71, -52, -43,
                     -35, 20, 31, 38, 43, 45, 46, 63, 68, 87, 90]
    L2: list[int] = [-91, -74, -62, -52, -11, -4, -2, 1, 95, 99]
    print(merge(sorted(L1), sorted(L2)))


if __name__ == "__main__":
    main()
