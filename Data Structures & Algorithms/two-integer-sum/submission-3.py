class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i, num in enumerate(nums):
            req = target - num
            if req in hmap:
                return [hmap[req], i]    
            if  num not in hmap:
                hmap[num] = i
            
                
