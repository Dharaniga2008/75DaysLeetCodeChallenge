class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        count = {}
        max_len = 0

        for right in range(len(fruits)):
            # Add fruit to basket
            count[fruits[right]] = count.get(fruits[right], 0) + 1

            # If more than 2 types, shrink window
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len