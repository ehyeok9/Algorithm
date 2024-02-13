import sys

input = sys.stdin.readline

def lcs(s1, s2):
    dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
    
    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
    
    print(dp[len(s1)-1][len(s2)-1])
    backTracking(dp, s1, s2)
        
def backTracking(dp, s1, s2):
    lcs = []
    y, x = len(dp)-1, len(dp[0])-1
    while y > 0 and x > 0:
        if dp[y][x] == dp[y-1][x]:
            y -= 1
        elif dp[y][x] == dp[y][x-1]:
            x -= 1
        else:
            lcs.append(s1[y])
            y -= 1
            x -= 1
            
    print("".join(lcs[::-1]))
        

if __name__ == "__main__":
    s1 = input().strip()
    s2 = input().strip()
    s1 = " " + s1
    s2 = " " + s2
    
    lcs(s1, s2)