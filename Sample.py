from typing import List


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

print('hello world')
        