class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if len(operations) == 1:
            return int(operations[0])
        record = []
        for i in range(len(operations)):
            if operations[i] == "C":
                record.pop()
            elif operations[i] == "D":
                d_val = (record[-1]) * 2
                record.append(d_val)
            elif operations[i] == "+":
                sum_ = (record[len(record) -1] + record[len(record) - 2])
                record.append(sum_)
            else:
                record.append(int(operations[i]))
        return sum(record)