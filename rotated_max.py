from typing import List

def max_index_in_rotated(arr: list[int]) -> int:
    if not arr:
        raise ValueError("array must be non-empty.")
    n = len(arr)
    if n == 1:
        return 0

    lo, hi = 0, n - 1
    if arr[lo] < arr[hi]:
        return hi

    while lo <= hi:
        mid = (lo + hi) // 2
        prev = (mid - 1 + n) % n
        nxt = (mid + 1) % n

        if arr[mid] >= arr[prev] and arr[mid] >= arr[nxt]:
            return mid

        if arr[lo] <= arr[mid]:
            lo = mid + 1
        else:
            hi = mid - 1

    raise RuntimeError("input must be a rotation of a strictly increasing array.")

def max_value_in_rotated(arr: list[int]) -> int:
    return arr[max_index_in_rotated(arr)]

if __name__ == "__main__":
    samples = [
        [35, 42, 5, 15, 27, 29],
        [27, 29, 35, 42, 5, 15],
    ]

    for a in samples:
        idx = max_index_in_rotated(a)
        print(f"array: {a}")
        print(f"maximum value: {a[idx]} at index {idx}")
        print("-" * 48)