# Using hashmaps
# Time: O(N*M), # of words * chars in each word
# Space: O(1) since we have 26 english letter only for the hashmap
def isAlienSorted(words, order: str) -> bool:
    order_hashmap = {}
    word2 = ""
    for i, char in enumerate(order):
        order_hashmap[char] = i

    for j in range(len(words) - 1):
        word1 = word2 if word2 else [order_hashmap[char] for char in words[j]]
        word2 = [order_hashmap[char] for char in words[j + 1]]

        for k in range(len(word1)):
            if k == len(word1):
                return False
            if word1[k] > word2[k]:
                return False
            elif word1[k] < word2[k]:
                break

    return True
