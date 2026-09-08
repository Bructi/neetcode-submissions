class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        n1 = len(nums)
        n = len(set(nums))

        if n == n1:
            return False
        else :
            return True