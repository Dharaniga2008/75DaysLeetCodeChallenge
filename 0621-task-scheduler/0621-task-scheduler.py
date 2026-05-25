from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)

        maxFreq = max(freq.values())

        # number of tasks having max frequency
        maxCount = sum(1 for f in freq.values() if f == maxFreq)

        # core formula
        partCount = maxFreq - 1
        partLength = n + 1

        minTime = partCount * partLength + maxCount

        # answer is max of total tasks or calculated schedule
        return max(len(tasks), minTime)