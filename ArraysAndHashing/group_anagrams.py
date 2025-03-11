from collections import defaultdict


# Time: O(n*m)
# Space: O(n*m)
def groupAnagrams(strs):
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26 # That's easier than having another map to save the count of the chars
        for c in s:
            count[ord(c) - ord("a")] += 1 # We are mapping each letter to an index starting from 0 for a --> 25 for z
        res[tuple(count)].append(s) # Tuple since Python doesn't allow mutable objs as keys

    return list(res.values())


print(groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
