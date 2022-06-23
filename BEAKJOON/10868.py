from sys import stdin

def segTree(node, start, end):
    if start == end:
        tree[node] = lit[start]
        return tree[node]
    else:
        tree[node] = min([segTree(node*2, start, (start+end)//2), segTree(node*2+1, (start+end)//2+1, end)])
        return tree[node]
    
def findMin(node, start, end, left, right):
    if left > end or right <start:
        return float('inf')
    if left <= start and end <= right:
        return tree[node]
    return min(findMin(node*2, start, (start+end)//2, left, right),findMin(node*2+1, (start+end)//2 +1, end, left, right))
    
n,m = map(int, stdin.readline().split())
tree = [0]*1000000
lit = [int(stdin.readline()) for i in range(n)]
segTree(1,0, n-1)

for i in range(m):
    a,b = map(int, stdin.readline().split())
    print(findMin(1,0,n-1,a-1,b-1))