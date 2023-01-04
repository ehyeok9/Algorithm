from sys import stdin

t = int(stdin.readline())

def hotel(h,w,n):
    h_cnt, w_cnt = 0,1
    if (n >= h) and (n%h != 0):
        w_cnt += (n//h)
        h_cnt += (n%h)
    elif (n%h ==0):
    	w_cnt += (n//h -1)
    	h_cnt = h
    else:
        h_cnt += n
    
    if (w_cnt < 10):
        print(str(h_cnt)+"0"+str(w_cnt))
    else:
        print(str(h_cnt) + str(w_cnt))

for i in range(t):
    q = list(map(int,stdin.readline().split()))
    hotel(q[0],q[1],q[2])