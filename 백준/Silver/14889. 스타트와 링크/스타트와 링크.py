import sys

input = sys.stdin.readline

mini = float("inf")

def dfs(team, idx):
    global board, N, visited, mini

    if len(team) == N//2:
        temp = getDiff(team)
        mini = min(temp, mini)
        return
    
    for i in range(idx, N):
        if visited[i] == False:
            visited[i] = True
            team.append(i)
            dfs(team, i)
            team.pop()
            visited[i] = False
            
def getDiff(team1):
    global total
    
    team2 = total - set(team1)
    team2 = list(team2)
    p1, p2 = calc(team1), calc(team2)

    return abs(p1- p2)
    
def calc(team):
    global board
    point = 0
    
    for i in range(len(team)):
        for j in range(i, len(team)):
            point += board[team[i]][team[j]] + board[team[j]][team[i]]
            
    
    return point

if __name__ == "__main__":
    
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    
    total = set([i for i in range(N)])
    visited = [False for i in range(N)]
    
    dfs([], 0)
    
    print(mini)