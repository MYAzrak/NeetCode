# One pointer
# Time: O(n+m) which are the sizes of the words
# Space: O(n+m)
def mergeAlternately(word1: str, word2: str) -> str:
    result = []
    temp = 0
    for i in range(len(word1)):
        if i == len(word2):
            result.append(word1[i:])
            return "".join(result)
        result.append(word1[i])
        result.append(word2[i])
        temp = i
    result.append(word2[temp + 1 :])
    return "".join(result)


print(mergeAlternately(word1="abc", word2="pqr"))
print(mergeAlternately(word1="ab", word2="pqrs"))
print(mergeAlternately(word1="abcd", word2="pq"))
