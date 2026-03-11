n, m = map(int, input().split())

# 0. 입력시 0의 위치를 저장해둠
# 1. 4방향 체크
# 2. visited == 0  --> append()
# 3. Queue가 다 비워졌으면?
# 4. 반복

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if not 0 <= x <= n-1 or not 0 <= y <= m-1:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        
        return True
    
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1
            
print(count)