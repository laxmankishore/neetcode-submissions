class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        index = 0
        result = []
        intervals.sort(key = lambda x:x[0])

        while index < n:
            if not result or result[-1][1] < intervals[index][0]:
                result.append(intervals[index])
            else:
                if result[-1][0] > intervals[index][0]:
                    result[-1][0] = intervals[index][0]
                if result[-1][1] < intervals[index][1]:
                    result[-1][1] = intervals[index][1]
            index += 1
        return result

    
            
        