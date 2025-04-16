# Time: O(max(m,n))
# Space: O(m+n)
def addBinary(a: str, b: str) -> str:
    result = ""
    carry = 0
    a, b = a[::-1], b[::-1]

    for i in range(max(len(a), len(b))):
        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0

        total = digit_a + digit_b + carry
        char = str(total % 2)
        result = char + result
        carry = total // 2

    if carry:
        result = "1" + result

    return result


print(addBinary(a="11", b="1"))
print(addBinary(a="1010", b="1011"))
