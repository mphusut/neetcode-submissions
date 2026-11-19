class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        options = {}

        for i in range(len(nums)):
            if (target - nums[i]) in options:
                return[options[target-nums[i]],i]
            else:
                options[nums[i]] = i
        
        