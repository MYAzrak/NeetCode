# DFS until len(unvisited) == 0
# Time: O(E+V)
# Space: O(E+V)
def countComponents(n: int, edges) -> int:
    if 0 <= n <= 1:
        return n

    adj_list = {i: [] for i in range(n)}
    unvisited = set([i for i in range(n)])
    components_num = 1

    for node1, node2 in edges:
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)

    def dfs(node, parent):
        if node in unvisited or parent == -1:
            if node in unvisited:
                unvisited.remove(node)

            for nei in adj_list[node]:
                if nei != parent:
                    dfs(nei, node)

    dfs(0, -1)

    while len(unvisited) != 0:
        components_num += 1
        dfs(unvisited.pop(), -1)

    return components_num


print(countComponents(n=6, edges=[[0, 1], [1, 2], [2, 3], [4, 5]]))
