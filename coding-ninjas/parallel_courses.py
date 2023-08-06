from collections import defaultdict


def parallelCourses(n, prerequisites):
    # Write your code here.
    graph = defaultdict(list)
    in_degree = [0 for _ in range(n + 1)]

    for req, course in prerequisites:
        graph[req].append(course)
        in_degree[course] += 1
    
    semesters = 0
    semester = [course for course in range(1, n + 1) if in_degree[course] == 0]
    courses_studied = 0

    while semester:
        next_semester = []

        for course in semester:
            courses_studied += 1

            for next_course in graph[course]:
                in_degree[next_course] -= 1

                if not in_degree[next_course]:
                    next_semester.append(next_course)
        
        semesters += 1
        semester = next_semester

    if courses_studied == n:
        return semesters
    
    return -1
