"""
Prob#1 Two Sum

Given an array of integers "nums" and an integer "target", return indices of the two numbers such that they add up to "target".

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example-1
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


# [ BRUTE FORCE APPROACH ]
nums = [2,11,8,7,15]
target = 9
n = len(nums)

for i in range(n):
    for j in range(i+1, n):
        if nums[i] + nums[j] == target:
            print(f"Nums are: {nums[i]}, {nums[j]}")