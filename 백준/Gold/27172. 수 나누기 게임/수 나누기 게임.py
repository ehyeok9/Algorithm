import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    cards = list(map(int, input().split()))
    
    size = max(cards)
    points = [[] for _ in range(size+1)]
    result = {}
    
    for card in cards:
        for j in range(card, size+1, card):
            points[j].append(card)
        result[card] = 0
        
    
    for card in cards:
        for num in points[card]:
            result[num] += 1
            result[card] -= 1
    
            
    for card in cards:
        print(result[card], end= " ")
    
    # print(*points)
    