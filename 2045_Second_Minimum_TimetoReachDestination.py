class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dist1 = [sys.maxsize] * (n + 1)
        dist2 = [sys.maxsize] * (n + 1)
        dist1[1] = 0
        heap = [(0, 1)] 

        while heap:
            t, node = heapq.heappop(heap)
            if node == n and t > dist1[n]:
                return t
            
            next_t = t + time
            if (t // change) % 2 == 1: 
                next_t += change - (t % change)

            for nei in adj[node]:
                if next_t < dist1[nei]:
                    dist2[nei], dist1[nei] = dist1[nei], next_t
                    heapq.heappush(heap, (next_t, nei))
                elif dist1[nei] < next_t < dist2[nei]:
                    dist2[nei] = next_t
                    heapq.heappush(heap, (next_t, nei))

        return -1