class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        result = [0] * length

        monoStack = [] # strict decreasing

        for index in range(length):
            curr_temp = temperatures[index]
            while monoStack and temperatures[monoStack[-1]] < curr_temp:
                process_index = monoStack.pop()
                result[process_index] = index - process_index
            monoStack.append(index)
        return result

        