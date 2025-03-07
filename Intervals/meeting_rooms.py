# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


# Brute force
# Time: O(n^2) because we are iterating through the list of intervals and then iterating through the list of busy times
# Space: O(n) because we are storing the busy times in a list
def canAttendMeetings(intervals) -> bool:
    busy = []
    for interval in intervals:
        if not busy:
            busy.append([interval.start, interval.end])
        else:
            for meeting in busy:
                if meeting[0] <= interval.start < meeting[1]:
                    return False
                if meeting[0] < interval.end <= meeting[1]:
                    return False
                if meeting[0] == interval.end:
                    meeting[0] = interval.start
                elif meeting[1] == interval.start:
                    meeting[1] = interval.end
            busy.append([interval.start, interval.end])
    return True


# Sorting
# Time: O(nlogn)
# Space: O(1)
def canAttendMeetings(intervals) -> bool:
    intervals.sort(key=lambda interval: interval.start)
    for i in range(len(intervals) - 1):
        if intervals[i].end > intervals[i + 1].start:
            return False
    return True
