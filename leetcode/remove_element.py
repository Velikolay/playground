from typing import List


def removeElement(nums: List[int], val: int) -> int:
    if not nums:
        return 0

    low, high = 0, len(nums) - 1
    while low < high:
        if nums[high] == val:
            high -= 1
            continue

        if nums[low] != val:
            low += 1
            continue

        if nums[low] == val:
            nums[low], nums[high] = nums[high], nums[low]

    return low if nums[low] == val else low + 1
