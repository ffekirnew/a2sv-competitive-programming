class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = { i: [] for i in range(numCourses) }
        in_degree = { i: 0 for i in range(numCourses) }
        
        for course, pre_requisite in prerequisites:
            in_degree[course] += 1
            graph[pre_requisite].append(course)
        
        queue = deque([course for course in graph.keys() if in_degree[course] == 0])
        order = []
        
        while queue:
            curr_course = queue.popleft()
            
            order.append(curr_course)
            
            for new_course in graph[curr_course]:
                in_degree[new_course] -= 1
                
                if in_degree[new_course] == 0:
                    queue.append(new_course)

        return len(order) == numCourses
            