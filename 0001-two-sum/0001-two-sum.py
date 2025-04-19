class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,num in enumerate(nums):
            complement = target-num
            if num in map:
                return [map[num], i]
            map[complement] = i