class Solution:
    def threeSum(self,nums):
        nums.sort()              # Step 1: sort array
        result = []
        n = len(nums)

        for i in range(n - 2):   # no need to go till n
        # Step 2: skip duplicate values of i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

        # Step 3: two-pointer search
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                # Step 4: skip duplicates for left & right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1   # need bigger sum
                else:
                    right -= 1  # need smaller sum

        return result