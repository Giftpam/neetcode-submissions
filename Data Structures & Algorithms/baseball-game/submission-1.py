class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                d_val = (stack[-1]) * 2
                stack.append(d_val)
            elif operations[i] == "+":
                sum_ = (stack[len(stack) -1] + stack[len(stack) - 2])
                stack.append(sum_)
            else:
                stack.append(int(operations[i]))
        return sum(stack)