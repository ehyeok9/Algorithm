import sys
import math

if __name__ == '__main__':
    a,b,c,d = map(int, sys.stdin.readline().split())

    # 원래 삼각형의 넓이 구하기
    s = (a + b + c)/2 
    value = s * (s-a)*(s-b)*(s-c)
    originalArea = math.sqrt(value)
    r = originalArea/s
    
    # 닮음 비율 구하기
    # 기준을 중앙값으로
    originalR = (2*originalArea)/(a+b+c)
    r = originalR - d
    ratio = pow(r, 2) / pow(originalR, 2)
    ratio = 1 - ratio
    print("{:.5f}".format(originalArea*ratio))