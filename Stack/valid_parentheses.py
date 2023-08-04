class Solution:
    def isValid(self, s: str) -> bool:
        valid_order = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for char in s:
            if char in valid_order.keys():
                if stack and stack[-1] == valid_order[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False


test = Solution()
print(test.isValid("]"))
