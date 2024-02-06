import sys

input = sys.stdin.readline

MODULER = 1000000007

# S/N = a/b

def calc(S, N): 
    inverse = powerAndModuler(N, MODULER-2)
    return S * inverse % MODULER

def powerAndModuler(N, power):
    if power == 1:
        return N
    
    if power % 2 == 0:
        val = powerAndModuler(N, power//2) % MODULER
        return val * val % MODULER
    else:
        val = powerAndModuler(N, (power-1)//2) % MODULER
        return N * val * val % MODULER
    
if __name__ == "__main__":
    M = int(input())
    dice = []
    for _ in range(M):
        dice.append(list(map(int, input().split())))
    
    result = 0
    for i in range(M):
        result += calc(dice[i][1], dice[i][0])
        result %= MODULER

    print(result)
        