# Time: O(m*n)
# Space: O(m*n)
def transpose(matrix):
    transpose = [[] for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            transpose[i].append(matrix[j][i])
    return transpose


print(transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
