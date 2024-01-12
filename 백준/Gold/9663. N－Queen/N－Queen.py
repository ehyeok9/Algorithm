import sys

input = sys.stdin.readline

n = int(input())
count = 0
loc = [0] * n

def check(row):
    for i in range(row):
        if loc[row] == loc[i] or abs(loc[row] - loc[i]) == row - i:
            return False
    return True
    
def queen(row):
    if row == n:
        global count
        count += 1
        return
    
    for col in range(n):
        loc[row] = col
        if check(row):
            queen(row + 1)
                
if __name__ == "__main__":
    location = []
    
    queen(0)
    
    print(count)
    