import sys
from collections import deque

input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def bfs(graph, n, m, visited):
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1

    while q:
        x, y, w = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][w]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '0' and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append([nx, ny, w])

                if graph[nx][ny] == '1' and w == 0:
                    visited[nx][ny][w + 1] = visited[x][y][w] + 1
                    q.append([nx, ny, w + 1])

    return -1

if __name__ == "__main__":
    n, m = map(int, input().split())

    route = []
    for _ in range(n):
        route.append(input().rstrip())

    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

    print(bfs(route, n, m, visited))
