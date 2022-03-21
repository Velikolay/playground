import math


def get_next_idx(limit, idx, offset):
    return (idx + offset) % limit


def rotate(arr, k):
    limit = len(arr)
    num_loops = math.gcd(len(arr), k)
    for start in range(num_loops):
        curr_val = arr[start]
        next_idx = get_next_idx(limit, start, k)
        next_val = arr[next_idx]

        while start != next_idx:
            arr[next_idx] = curr_val
            next_idx = get_next_idx(limit, next_idx, k)
            curr_val = next_val
            next_val = arr[next_idx]
        arr[next_idx] = curr_val
    return arr


if __name__ == "__main__":
    print(rotate([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12))
    print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
    print(rotate([-1, -100, 3, 99], 2))
    print(rotate([-1, -100, 3, 99, 2, 6], 2))
