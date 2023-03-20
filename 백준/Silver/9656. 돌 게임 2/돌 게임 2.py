import sys
    
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    if (n % 2 == 0):
        print("SK")
    else:
        print("CY")
    
    # 1 = 1 cy
    # 2 = 1 1 sk
    # 3 = 1 1 1 cy
    # 4 = 3 1 sk 
    # 5 = 3 1 1 cy
    # 6 = 1 3 1 1 sk
    # 7 = 3 3 1 cy 
    # 8 = 3 3 1 1 sk