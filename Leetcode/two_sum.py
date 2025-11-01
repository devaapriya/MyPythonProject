from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for index, value in enumerate(nums):
            secVal = target - value

            if secVal in output:
                return [output[secVal], index]

            output[value] = index



if __name__ == "__main__" :
    sol_obj = Solution()
    nums = [3, 2, 7, 15]
    target = 9
    result = sol_obj.twoSum(nums, target)