from functools import total_ordering
import math
import sys
from collections import deque

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    input = list(map(int, sys.stdin.readline().split()))
    
    tval = sum(input)
    if (tval%3 != 0):
        print("NO")
    else:
        two = 0
        one = 0
        
        for val in input:
            two += val//2
            if (val%2 == 1): one += 1
        # print(two, one)
        
        if (two < one): print("NO")
        elif (two == one): print("YES")
        elif (two > one):
            a =two-one
            if a%3==0:
                print("YES")
            else:
                print("NO")
            # print(total)
            # if (total%2 == 0): print("YES")
            # else: print("NO")