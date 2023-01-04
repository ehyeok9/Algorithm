from sys import stdin

def palindrom(num):
	qq = str(num)
	u = ""
	
	for i in range(len(qq)-1, -1, -1):
		u += qq[i]
		
	if (qq == u):
		print("yes")
	else:
		print("no")
		
while True:
	k = int(stdin.readline())
	if (k == 0):
		break
	palindrom(k)