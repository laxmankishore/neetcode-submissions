class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                a = stack[-1]
                b = stack[-2]
                stack.append(a + b)
            elif op == "D":
                val = stack[-1]
                stack.append(val * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)

        