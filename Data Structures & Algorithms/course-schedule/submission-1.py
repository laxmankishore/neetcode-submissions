class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pmap = {course : [] for course in range(numCourses)}
        for course, preq in prerequisites:
            pmap[course].append(preq)
        
        ##pmap : {0:[1], 1:[2], 2 :[]}

        cycle = set()
        seen = set()

        def dfs(course):
            if course in cycle:
                return False
            
            if (course in seen):
                return True
            
            if pmap[course] == [] :
                seen.add(course)
                return True

            cycle.add(course)
            for preq in pmap[course]: ## course 0 has preq 1, 2
                if not dfs(preq):
                    return False
            
            seen.add(course)
            cycle.remove(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            
