class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        stack = []
        result = [0] * length

        for index in range(length):
            while stack and stack[-1][0] < temperatures[index]:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = index - stack_index
            stack.append((temperatures[index], index))
        return result

        