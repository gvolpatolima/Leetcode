class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pointer = 0
        n = len(nums)

        for i in range (n):
            for j in range(i + 1, n):
                pair_sum = nums[i] + nums[j]
                if pair_sum == target:
                    result = [i,j]
                    return result

