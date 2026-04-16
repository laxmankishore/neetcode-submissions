class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connected_count = 0

        adjlist = {node:[] for node in range(n)}

        for u,v in edges :
            adjlist[u].append(v)
            adjlist[v].append(u)
        
        visited = set()
        
        def dfs(src):
            visited.add(src)
            for neighbor in adjlist[src]:
                if neighbor not in visited : 
                    dfs(neighbor)

            
        for node in adjlist:
            if node not in visited:
                dfs(node)
                connected_count += 1
        
        return connected_count

        

