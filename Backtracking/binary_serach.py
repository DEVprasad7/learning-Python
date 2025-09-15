# checking if a target int is present in a sorted array or not

def binary_serach(nums: list[int], target: int) -> bool:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return True
        elif target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1

    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 10

    print(binary_serach(nums, target)) # False