import sys
from bisect import bisect_right


def pairs(k, arr):
    arr = sorted(arr)
    c = 0
    for i in range(len(arr)):
        z = bisect_right(arr, arr[i] + k, i)
        if arr[z - 1] == arr[i] + k:
            c += 1
    return c


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = pairs(k, arr)
    print(result)