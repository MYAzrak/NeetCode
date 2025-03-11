# When encoding, add the length of each word in the beginning + a
# delimiter to separate b/w them. The length can be more than 1 digit.
# Time: O(N)
# Space: O(N)
def encode(strs) -> str:
    encoded = ""
    for word in strs:
        encoded += str(len(word)) + "#" + word
    return encoded


def decode(s: str):
    decoded = []
    i, j = 0, 0

    while i < len(s):
        while s[j] != "#":
            j += 1
        word_len = int(s[i:j])
        i = j + 1
        decoded.append(s[i : i + word_len])
        j = i + word_len
        i = j

    return decoded


print(encode(["we", "say", ":", "yes"]))
print(decode(encode(["we", "say", ":", "yes"])))
