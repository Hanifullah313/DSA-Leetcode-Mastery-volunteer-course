from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       pmap ={}
       for i , n in enumerate(nums):
            dif = target - n
            if dif in pmap:
                return [pmap[dif],i]

            pmap[n]=i

       return [] # Return empty if no solution is found