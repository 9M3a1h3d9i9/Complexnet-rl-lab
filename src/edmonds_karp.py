import numpy as np
from collections import deque
from typing import List, Tuple

def bfs_augmenting_path(cap: np.ndarray, flow: np.ndarray, s: int, t: int) -> Tuple[List[Tuple[int,int]], float]:
    n = cap.shape[0]
    parent = [-1] * n
    parent[s] = s
    q = deque([s])
    
    while q:
        u = q.popleft()
        for v in range(n):
            residual = cap[u, v] - flow[u, v]
            if residual > 1e-6 and parent[v] == -1:
                parent[v] = u
                if v == t:
                    path = []
                    bottleneck = float('inf')
                    cur = t
                    while cur != s:
                        prev = parent[cur]
                        path.append((prev, cur))
                        bottleneck = min(bottleneck, cap[prev, cur] - flow[prev, cur])
                        cur = prev
                    path.reverse()
                    return path, bottleneck
                q.append(v)
    return [], 0.0

def edmonds_karp_max_flow(cap: np.ndarray, s: int, t: int) -> Tuple[float, np.ndarray]:
    n = cap.shape[0]
    flow = np.zeros((n, n), dtype=float)
    maxflow = 0.0
    
    while True:
        path, bottleneck = bfs_augmenting_path(cap, flow, s, t)
        if bottleneck == 0.0:
            break
        maxflow += bottleneck
        for u, v in path:
            flow[u, v] += bottleneck
            flow[v, u] -= bottleneck
    return maxflow, flow

def min_cut_from_flow(cap: np.ndarray, flow: np.ndarray, s: int) -> Tuple[List[int], List[int]]:
    n = cap.shape[0]
    visited = [False] * n
    stack = [s]
    visited[s] = True
    
    while stack:
        u = stack.pop()
        for v in range(n):
            residual = cap[u, v] - flow[u, v]
            if residual > 1e-6 and not visited[v]:
                visited[v] = True
                stack.append(v)
    
    S = [i for i in range(n) if visited[i]]
    T = [i for i in range(n) if not visited[i]]
    return S, T
