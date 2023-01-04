# Hello World program in Python
    
from sys import stdin

n,m = map(int, stdin.readline().split())

obj = stdin.readlines()
	
bl_wh = ["", ""]
	
for i in range(8):
	if i%2 == 0:
		bl_wh[0] += "B"
		bl_wh[1] += "W"
	else:
		bl_wh[0] += "W"
		bl_wh[1] += "B"
		
black = []
white = []

for i in range(8):
	if i%2 == 0:
		black.append(bl_wh[0])
		white.append(bl_wh[1])
	else:
		black.append(bl_wh[1])
		white.append(bl_wh[0])
		
total = []
col = 0
row = 0

for i in range(n-7):
	for j in range(m-7):
		row = 0
		bl = 0
		wh = 0
		for k in range(i,8+i):
			col = 0
			for l in range(j, 8+j):
				if obj[k][l] != black[row][col]:
					bl += 1
				if obj[k][l] != white[row][col]:
					wh += 1
				col += 1
			row += 1
		total.append(bl)
		total.append(wh)

print(min(total))