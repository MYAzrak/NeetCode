# DFS to detect loops if we visited a node that is already in the visited set (since this is
# undirected, we need to skip checking the parent of the node). Also we need to make sure
# that all of the nodes are one component (e.g. not 2 trees) so we need to check if
# len(visited) == n
# Time: O(V+E)
# Space: O(V+E)
def validTree(n: int, edges) -> bool:
    if not n:
        return True

    adj_list = {i: [] for i in range(n)}

    for node1, node2 in edges:
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)

    visited = set()

    def dfs(node, parent):
        if node in visited:
            return False

        visited.add(node)

        for nei in adj_list[node]:
            if nei != parent:
                if not dfs(nei, node):
                    return False

        return True

    return dfs(0, -1) and len(visited) == n


print(validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]]))
