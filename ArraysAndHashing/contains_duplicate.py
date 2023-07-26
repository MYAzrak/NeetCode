from collections import Counter
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return any(num != 1 for num in Counter(nums).values())
