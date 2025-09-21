from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        summ = sum(piles)
        maxx = max(piles)
        i = maxx
        while i > 1 and (summ // i) < h:
            i -= 1
        return i + 1

c = Solution()

print(c.minEatingSpeed([25,10,23,4], 4))


