import sys

input = sys.stdin.readline

maxi = 0

def dfs(val, idx):
    global maxi, schedule
    
    if idx > N:
        return
    
    maxi = max(maxi, val)
    # print(maxi, idx)
    for i in range(idx, N):
        dfs(val + schedule[i][1], i + schedule[i][0])
            

if __name__ == "__main__":
    N = int(input())
    schedule = []
    for _ in range(N):
        schedule.append(list(map(int, input().split())))

    dfs(0, 0)
    
    print(maxi)
        
    
    