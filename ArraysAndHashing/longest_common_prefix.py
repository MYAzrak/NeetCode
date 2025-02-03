# Time complexity: O(n∗m)
# Where n is the length of the shortest string and m is the number of strings.
# Space complexity: O(1)
def longestCommonPrefix(strs):
    longest_prefix = ""
    shortest_string = min(strs, key=len)
    n = len(shortest_string)
    for i in range(n):
        for word in strs:
            if shortest_string[i] != word[i]:
                return longest_prefix
        longest_prefix += shortest_string[i]
    return longest_prefix
