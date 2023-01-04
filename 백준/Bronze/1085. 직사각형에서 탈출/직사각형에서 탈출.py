x,y,w,h = map(int, input().split())

a = h - y
b = w - x

print(min(x,y,a,b))

