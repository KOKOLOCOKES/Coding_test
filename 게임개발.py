# 캐릭터가 있는 장소는 1*1 크기의 정사각형으로 이루어진 N*M  크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다.
# 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.

# 캐릭터의 움직임 설정
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로가고 1단계로 돌아간다. 단 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

# 첫째 줄에 맵의 세로 크기 N과 가로 크기 M이 공백으로 구분되어 입력된다. (3 <= N, M <= 50)
# 둘째 줄에 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방향 d가 공백으로 구분되어 입력된다. (0: 북, 1: 동, 2: 남, 3: 서)
# 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 북쪽부터 남쪽 순서대로 한 줄씩 입력된다. 육지는 0, 바다는 1로 표시된다. 맵의 외곽은 항상 바다로 되어있다.
# 처음에 캐릭터가 위치한 칸의 상태는 항상 육지이다.

# 출력 조건: 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.

n, m = map(int, input().split())
row, column, direction = map(int, input().split())

move = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북 - 동 - 남 - 서

island = [] # 지도
exp_island = [[0] * m for _ in range(n)] #가본 곳 체크
for _ in range(n):
    temp = list(map(int, input().split()))
    island.append(temp)

# 1단계: 왼쪽 회전
def turn_left():
    global direction
    
    if direction == 0:
        direction = 3
        
    else:
        direction -= 1

# 3단계 정의
def end_check() -> bool:
    global row, column, direction
    
    for dx, dy in move:
        tmp_r = row + dx
        tmp_c = column + dy
        
        if island[tmp_r][tmp_c] == 0 and exp_island[tmp_r][tmp_c] == 0:
            return True
    
    # 뒤로 이동할 곳이 있을 경우
    if island[row - move[direction][0]][column - move[direction][1]] == 0:
        row -= move[direction][0]
        column -= move[direction][1]
        return True
    
    # 뒤로 이동할 곳이 없을 경우
    else:
        return False
    
running = True

# 초기 위치 방문 설정
count = 1
exp_island[row][column] = 1

while running:
    turn_left()
    dx, dy = move[direction]
    
    if island[row + dx][column + dy] != 1 and exp_island[row + dx][column + dy] == 0:
        row += dx
        column += dy
        
        exp_island[row][column] = 1
        count += 1
        
    running = end_check()
    
    print(row, column, direction, count) 
    
    
print(count)
