import sys
from collections import deque

flag = False
def dfs(pmap, snode, enode, visited):
    deq = deque()
    deq.append([snode, 0])
    result = []
    
    while deq:
        node, cnt = deq.popleft()
        
        if (node == enode): result.append(cnt)
        if (node in visited): continue
        visited.append(node)
        for i in pmap[node]:
            deq.append([i, cnt+1])
    
    return min(result)
            
    
    

    
if __name__=="__main__":
    n, m = map(int, sys.stdin.readline().split())
    pmap = {}
    for i in range(1,n+1):
        pmap[i]= []
    
    for i in range(m):
        p1, p2 = map(int, sys.stdin.readline().split())
        if (p2 not in pmap[p1]): pmap[p1].append(p2)
        if (p1 not in pmap[p2]): pmap[p2].append(p1)

    kb = []
    for i in range(1,n+1):
        temp = 0
        for j in range(1,n+1):
            if (i==j): continue
            visited = []
            temp += dfs(pmap, i, j, visited)
        kb.append(temp)
    # print(kb)
        
    mnum = min(kb)
    for i in range(len(kb)):
        if (kb[i] == mnum):
            print(i+1)
            break
    
    