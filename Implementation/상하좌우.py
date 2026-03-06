#첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1 <= N <= 100)
#둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1 <= 이동 횟수 <= 100)

#출력 조건: 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백으로 구분하여 출력한다. 단, 여행가 A의 처음 위치는 (1, 1)이다.

n = int(input())
move = list(map(str, input().split()))

direction = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
x, y = 1, 1

for i in move:
    temp = direction[i]
    if 1 <= x + temp[0] <= n and 1 <= y + temp[1] <= n:
        x += temp[0]
        y += temp[1]
    
print(x, y)
