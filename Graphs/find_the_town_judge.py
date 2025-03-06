from collections import defaultdict


# Using hashmaps
# Time: O(n + e) where n is the number of people and e is the number of edges
# Space: O(n) where n is the number of people
def findJudge(n: int, trust) -> int:
    # i.e got trust from someone
    incoming_edge = {person: 0 for person in range(1, n + 1)}
    # i.e. gave trust to someone
    outgoing_edge = {person: 0 for person in range(1, n + 1)}
    # Or you can use defaultdict(int) from collections for incoming_edge and outgoing_edge

    for src, des in trust:
        outgoing_edge[src] += 1
        incoming_edge[des] += 1

    for key, val in outgoing_edge.items():
        if val == 0:
            if incoming_edge[key] == n - 1:
                return key

    return -1


# Same but with one hashmap since only the judge will have incoming - outgoing = n - 1
def findJudge(n: int, trust) -> int:
    delta = defaultdict(int)

    for src, dst in trust:
        delta[src] -= 1
        delta[dst] += 1

    for i in range(1, n + 1):
        if delta[i] == n - 1:
            return i

    return -1
