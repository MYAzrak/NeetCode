# Using a stack
# Time: O(N)
# Space: O(N)
def calPoints(operations) -> int:
    records = []
    for operation in operations:
        if operation == "+":
            records.append(records[-1] + records[-2])
        elif operation == "D":
            records.append(records[-1] * 2)
        elif operation == "C":
            records.pop()
        else:  # int
            records.append(int(operation))
    return sum(records)


print(calPoints(operations=["5", "2", "C", "D", "+"]))
print(calPoints(operations=["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(calPoints(operations=["1", "C"]))
