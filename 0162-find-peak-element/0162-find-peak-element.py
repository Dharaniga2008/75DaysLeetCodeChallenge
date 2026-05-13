class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If middle element is smaller than next element
            # then peak is on the right side
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                # Peak is on the left side including mid
                right = mid

        return left