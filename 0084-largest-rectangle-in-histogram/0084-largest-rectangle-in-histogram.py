class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # stores indices
        max_area = 0
        n = len(heights)

        for i in range(n):
            # Process when current height is smaller
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                
                # width calculation
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                
                max_area = max(max_area, h * width)
            
            stack.append(i)

        # Process remaining bars in stack
        while stack:
            h = heights[stack.pop()]
            
            if stack:
                width = n - stack[-1] - 1
            else:
                width = n
            
            max_area = max(max_area, h * width)

        return max_area