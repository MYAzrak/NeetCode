# Cycle detection using DFS
# Time: O(N+E) number of nodes + number of edges (from prerequisites)
# Space: O(N+E)
def canFinish(numCourses: int, prerequisites) -> bool:
    course_pre = {i: [] for i in range(numCourses)}
    for course, pre in prerequisites:
        course_pre[course].append(pre)

    visited = set()

    def dfs(course):
        if course in visited:
            return False
        if not course_pre[course]:
            return True

        visited.add(course)
        for pre in course_pre(course):
            if not dfs(pre):
                return False

        # We finished visiting a course and its prerequisites --> remove it
        # from visited and treat it as a course with no prerequisites
        visited.remove(course)
        course_pre[course] = []
        return True

    for course_num in range(numCourses):
        if not dfs(course_num):
            return False

    return True


print(canFinish(numCourses=2, prerequisites=[[0, 1], [2, 3], [1, 2], [3, 0]]))
