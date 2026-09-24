class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indeg = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            indeg[dst] += 1
            adj[src].append(dst)
        
        q = deque()

        result = []

        for n in range(numCourses):
            if indeg[n] == 0:
                q.append(n)
        
        while q:
            node = q.popleft()
            result.append(node)
            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        if len(result) == numCourses:
            return result[::-1]
        else: 
            return []


        