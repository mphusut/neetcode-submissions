class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {}

        for i in nums:
            majority[i] = majority.get(i,0) + 1
        for k,v in majority.items():
            if v > len(nums)/2:
                return k

        