
from collections import deque

# 체스말 좌표
dx = [+2, +1, -1, -2, -2, -1, +1, +2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]


def bfs(a, b, c, d):
    queue = deque()
    queue.append((a, b))

    while queue:
        curX, curY = queue.popleft() # 현재 위치
        if curX == c and curY == d:
            print(visited[curX][curY] - 1)
            return True

        for i in range(8): # 좌표마다 반복
            nx = curX + dx[i]
            ny = curY + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if visited[nx][ny] == 0: # 방문하지 않았을 시
                visited[nx][ny] = visited[curX][curY] + 1
                queue.append((nx, ny))

    return False


n = int(input())
for i in range(n):
    l = int(input())
    visited = [[0] * l for _ in range(l)]
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    visited[a][b] = 1
    bfs(a, b, c, d)