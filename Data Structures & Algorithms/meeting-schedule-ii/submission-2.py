"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        min_heap = []

        cars = 0

        intervals.sort(key=lambda interval: interval.start)

        for interval in intervals:
            last_car = None
            if min_heap and min_heap[0][0] <= interval.start:
                end_time, car_id = heapq.heappop(min_heap)
                heapq.heappush(min_heap, (interval.end, car_id))
            else:
                heapq.heappush(min_heap, (interval.end, cars))
                cars +=1
        
        return cars