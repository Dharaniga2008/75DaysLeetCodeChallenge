# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left = 1
        right = n
        
        while left < right:
            
            mid = left + (right - left) // 2
            
            # If mid version is bad,
            # first bad version can be mid or before mid
            if isBadVersion(mid):
                right = mid
            
            # If mid version is good,
            # first bad version must be after mid
            else:
                left = mid + 1
        
        return left