# Using sorting
# Time: O(nlogn)
# Space: O(1) Assuming that sorted doesn't need any space
def isAnagram(s, t):
    return list(s).sort() == list(t).sort()


print(isAnagram("anagram", "nagaram"))


# Using Hashmaps
# Time: O(n)
# Space: O(n)
def isAnagram(s, t):
    if len(s) != len(t):  # Saves some time
        return False
    s_map = {}
    t_map = {}

    for i in range(len(s)):
        if s[i] in s_map.keys():
            s_map[s[i]] += 1
        else:
            s_map[s[i]] = 1

        if t[i] in t_map.keys():
            t_map[t[i]] += 1
        else:
            t_map[t[i]] = 1

    return s_map == t_map


print(isAnagram("anagram", "nagaram"))
print(isAnagram("car", "rat"))
