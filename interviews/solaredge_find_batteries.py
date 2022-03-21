from typing import List, Optional


def find_batteries(capacity: int, batteries: List[int]) -> Optional[List[int]]:
    b1, b2 = batteries[0], batteries[1]
    curr_capacity = capacity

    while curr_capacity > b1:
        num_b1 = curr_capacity // b1
        remaining = capacity - num_b1 * b1
        if remaining % b2 == 0:
            return [num_b1, remaining // b2]

        curr_capacity -= b1

    if capacity % b2 == 0:
        return [0, capacity // b2]

    return None


if __name__ == "__main__":
    print(find_batteries(24, [10, 7]))
    print(find_batteries(70, [10, 7]))
    print(find_batteries(25, [10, 7]))
    print(find_batteries(7, [10, 7]))
    print(find_batteries(28, [10, 7]))
    print(find_batteries(27, [10, 7]))
