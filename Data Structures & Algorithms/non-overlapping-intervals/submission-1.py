class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals length <= 1 return 0
        # sort the intervals by end time
        # greedily choose the first one
        # loop through sorted intervals, each time we take
        # an interval, we check if it overlaps with the last
        # interval we took
        # each time we overlap, we increment a counter
        # return counter

        if len(intervals) <= 1:
            return 0

        # n log n
        # sorted_intervals = sorted(intervals, key = lambda interval: interval[1])
        intervals.sort(key = lambda interval: interval[1])

        # guaranteed at least 2 intervals

        last_taken_interval = intervals[0]
        remove_counter = 0

        for interval in intervals[1:]:
            if interval[0] < last_taken_interval[1]:
                remove_counter += 1
            else:
                last_taken_interval = interval
        return remove_counter