from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        graph = defaultdict(list)
        visit = [0] * numCourses  # 0=unvisited,1=visiting,2=visited
        
        for a, b in prerequisites:
            graph[b].append(a)
        
        def dfs(node):
            if visit[node] == 1:
                return False
            if visit[node] == 2:
                return True
            
            visit[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visit[node] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True