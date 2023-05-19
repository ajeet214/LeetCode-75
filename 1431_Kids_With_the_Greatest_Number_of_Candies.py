from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if candy+extraCandies >= max(candies) else False for candy in candies]


obj = Solution()
print(obj.kidsWithCandies([2,3,5,1,3], 3))
"""
Runtime: 56 ms
Memory: 16.2 MB
"""