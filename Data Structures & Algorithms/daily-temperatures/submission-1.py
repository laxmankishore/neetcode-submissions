class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        result = [0] * length

        monoStack = [] # strictly decreasing [(temp, day)]

        for day in range(length):
            curr_temp = temperatures[day]
            while monoStack and curr_temp > monoStack[-1][0]:
                ## performing pop and process the day
                temp = monoStack.pop()
                result[temp[1]] = day - temp[1]
            monoStack.append((curr_temp, day))
        return result
