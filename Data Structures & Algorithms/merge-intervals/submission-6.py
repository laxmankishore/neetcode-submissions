class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])
        for index in range(len(intervals)):
            curr_interval = intervals[index]
            if not result or result[-1][1] < curr_interval[0]:
                result.append(curr_interval)
            else :
                if result[-1][1] >= curr_interval[0] and result[-1][1] < curr_interval[1]:
                    result[-1][1] = curr_interval[1]
                
        return result         


        