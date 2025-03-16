# Using a Stack
# Time: O(n)
# Space: O(n)
def evalRPN(tokens) -> int:
    stack = []

    for char in tokens:
        try:
            num = int(char)
            stack.append(num)
        except:
            num2 = stack.pop()
            num1 = stack.pop()
            if char == "+":
                stack.append(num1 + num2)
            elif char == "-":
                stack.append(num1 - num2)
            elif char == "*":
                stack.append(num1 * num2)
            elif char == "/":
                stack.append(int(num1 / num2))

    return stack[-1]


print(
    evalRPN(
        tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)
