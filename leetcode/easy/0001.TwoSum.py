from typing import List

# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rtnList = [];
        for  i in range(len(nums)):
            # 두 수의 합
            for j in range(i, len(nums)):
                if i == j:
                    continue
                    
                if nums[i] + nums[j] == target:
                    rtnList.append(i)
                    rtnList.append(j)
        return rtnList

nums = [2,7,11,15]
target = 9

sol = Solution()
rtnVal = sol.twoSum(nums, target)

print("\n");
print(rtnVal)