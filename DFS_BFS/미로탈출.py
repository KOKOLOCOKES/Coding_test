from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 이동 방향
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i, j in move:
            temp_x = x + i
            temp_y = y + j
            
            if not 0 <= temp_x <= n-1 or not 0 <= temp_y <= m-1:
                continue
            
            if graph[temp_x][temp_y] == 0:
                continue
            
            if graph[temp_x][temp_y] == 1:
                graph[temp_x][temp_y] = graph[x][y] + 1
                queue.append((temp_x, temp_y))
    
    return graph[n-1][m-1]

print(bfs(0, 0))