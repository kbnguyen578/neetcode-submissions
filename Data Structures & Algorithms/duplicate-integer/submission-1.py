class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # APPEARS more than once => count() method 
        # NONO => O(n) complexity... 

        seen = set() # hash to keep what we have seen, O(1) lookup
        for num in nums:
            if num in seen: 
                return True
            seen.add(num)
        return False
