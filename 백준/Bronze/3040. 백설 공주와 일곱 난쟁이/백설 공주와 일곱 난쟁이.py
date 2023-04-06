import sys

global input
global visited

def combination(array, start, n, r):
    if (r == 0):
        if (sum(array) == 100):
            for i in range(len(array)-1, -1, -1):
                print(array[i])
        return
    
    for i in range(start, n):
        visited[i] = True
        array[r-1] = input[i] 
        combination(array, i+1, n, r-1)
        visited[i] = False


if __name__ == "__main__":
    input = []
    for i in range(9):
        input.append(int(sys.stdin.readline()))
    visited = [False for _ in range(len(input))]
    array = [0]*7
    combination(array, 0, 9, 7)
    