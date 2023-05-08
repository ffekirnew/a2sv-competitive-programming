class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = { i: set() for i in range(numCourses) }
        color = { i: 'w' for i in range(numCourses) }
        in_degree = { i: 0 for i in range(numCourses) }
        
        for course, pre_requisite in prerequisites:
            graph[pre_requisite].add(course)
            in_degree[course] += 1
            
        def dfs(course):            
            color[course] = 'g'

            for new_course in graph[course]:
                if color[new_course] == 'g':
                    return

                if color[new_course] == 'w':
                    dfs(new_course)
                
            color[course] = 'b'
            order.append(course)

        order = []
        stack = [course for course in graph if in_degree[course] == 0]
        
        for course in stack:
            dfs(course)

        return reversed(order) if len(order) == numCourses else []
            