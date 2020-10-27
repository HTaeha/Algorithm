from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - num1

            if num2 in d:
                return [i, d[num2]]
            else:
                d[num1] = i

if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))
