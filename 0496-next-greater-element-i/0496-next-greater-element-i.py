class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nge_map = {}

        # Step 1: Process nums2
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                nge_map[smaller] = num
            stack.append(num)

        # Step 2: Remaining elements → no next greater
        while stack:
            nge_map[stack.pop()] = -1

        # Step 3: Build answer for nums1
        return [nge_map[num] for num in nums1]