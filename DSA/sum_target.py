"""1. Two Sum Problem

Difficulty: Easy
Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.
Key Concepts: Hashing, arrays, brute force vs. optimized approach."""


# nums = [2,3,5,6,4]
# target = 9


# def two_sum_target(nums, target):
#     result = []
    
#     for i in nums:
#         for j in nums:
#             if i + j == target:
#                 result.append((i, j))
#                 return result[0]

# print(two_sum_target(nums, target))





"""2. Reverse Words in a String

Difficulty: Easy–Medium
Problem: Given a string s, reverse the order of words in the string.
Example: " hello world " → "world hello".
Key Concepts: String manipulation, trimming spaces, stack/array split."""


s = "hello world"

def reverse_string(s):
    
    reversed_string = s[::-1]
    return reversed_string
    # l = len(s)
    # result = ""
    # for word in range(l-1, -1, -1):
    #     result += s[word]
    # return result

print(reverse_string(s))
        







# def two_sum_target_optimized(nums, target):
#     num_map = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_map:
#             return (num_map[complement], i)
#         num_map[num] = i
#     return None



            