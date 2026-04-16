class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {crs : [] for crs in range(numCourses)} 
        for crs, preq in prerequisites:
            adjlist[crs].append(preq)
        
        ## {0:[1]}
        ## {1:[2, 3]}
        # {2:[]}
        # {3:[]}
        visiting = set()

        def dfs(crs):
            if crs in visiting : 
                return False
            
            if adjlist[crs] == []:
                return True
            
            visiting.add(crs)

            for preq in adjlist[crs]:
                if not dfs(preq):
                    return False
            
            visiting.remove(crs)
            adjlist[crs] = []
            return True

        for crs in adjlist:
            if dfs(crs) == False:
                return False
        
        return True



