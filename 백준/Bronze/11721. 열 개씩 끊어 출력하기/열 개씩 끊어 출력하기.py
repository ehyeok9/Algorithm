moonjang = str(input())

sutja = len(moonjang)

for i in range(sutja):
    print(moonjang[i], end = '')
    if ((i+1) % 10) == 0:
        print(" ")