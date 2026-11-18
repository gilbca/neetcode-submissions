class Solution:

    def calPoints(self, operations: List[str]) -> int:
        record = []
        while operations:
            op = operations.pop(0)

            if op == "+":
                record.append(record[-2]+record[-1])
            elif op == "C":
                record.pop(-1)
            elif op == "D":
                n = record[len(record)-1] * 2
                record.append(n)
            else:
                record.append(int(op))
        i = 0
        for n in record:
            i += n
        return i