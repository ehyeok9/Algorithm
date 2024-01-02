import sys

input = sys.stdin.readline

def LCS_DP(x, y):
    dp = [[0 for i in range(len(y)+1)] for j in range(len(x)+1)]
    
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            if (x[i-1] == y[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    
    # for val in dp:
    #     print(val)
    # lcs = backtracking(dp, len(x), len(y))
    return dp[len(x)][len(y)]



def backtracking(dp, i, j):
    lcs = []
    while (i > 0 and j > 0):
        if (dp[i][j] == dp[i-1][j]):
            i -= 1
        elif (dp[i][j] == dp[i][j-1]):
            j -= 1
        else:
            lcs.append(x[i-1])
            i -= 1
            j -= 1
    return lcs[::-1]

if __name__ == "__main__":
    x = input().rstrip()
    y = input().rstrip()
    
    print(LCS_DP(x, y))
    