# Using a stack
# Time: O(n)
# Space: O(n)
def isValid(s: str) -> bool:
    stack = []
    valid_parentheses = {"[": "]", "{": "}", "(": ")"}
    for char in s:
        if char not in valid_parentheses:
            if stack and valid_parentheses[stack[-1]] == char:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False


print(isValid(s="()"))
print(isValid(s="()[]{}"))
print(isValid(s="(]"))
print(isValid(s="([])"))
