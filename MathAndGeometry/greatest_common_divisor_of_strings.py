# Time: O(min(m,n) * (m+n))
# Space: O(m+n) where m and n are the lengths of str1 & str2
def gcdOfStrings(str1: str, str2: str) -> str:
    def is_divisor(s, t):
        return s == t * (len(s) // len(t))

    gcd = min(str1, str2, key=len)

    while gcd:
        if len(str1) % len(gcd) == 0 and len(str2) % len(gcd) == 0:
            if is_divisor(str1, gcd) and is_divisor(str2, gcd):
                return gcd
        gcd = gcd[:-1]

    return ""


print(gcdOfStrings(str1="ABCABC", str2="ABC"))
print(gcdOfStrings(str1="ABABAB", str2="ABAB"))
print(gcdOfStrings(str1="LEET", str2="CODE"))
