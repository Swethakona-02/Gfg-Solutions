from collections import deque
class Solution:
    def minimumEdgeReversal(self, edges: list[list[int]], n: int, src: int, dst: int) -> int:
            graph = [[] for _ in range(n + 1)]

            for u, v in edges:
                graph[u].append((v, 0))
                graph[v].append((u, 1))

            dist = [float('inf')] * (n + 1)
            dist[src] = 0

            dq = deque([src])

            while dq:
                node = dq.popleft()

                for neighbor, cost in graph[node]:
                    new_dist = dist[node] + cost

                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist

                        if cost == 0:
                            dq.appendleft(neighbor)
                        else:
                            dq.append(neighbor)

            return dist[dst] if dist[dst] != float('inf') else -1
