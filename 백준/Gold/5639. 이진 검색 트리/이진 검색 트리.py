import sys

input = sys.stdin.readline

global bst

def postOrder(left, right):
    if left >= right: return
    
    mid = left+1
    for i in range(left+1, right):
        if bst[left] < bst[i]:
            mid = i
            break
        
    postOrder(left+1, mid)
    postOrder(mid, right)
    print(bst[left])
    
if __name__ == "__main__":
    sys.setrecursionlimit(10**7)
    
    bst = []
    while True:
        try:
            value = int(input())
        except:
            break
        bst.append(value)
    
    postOrder(0, len(bst))
    
