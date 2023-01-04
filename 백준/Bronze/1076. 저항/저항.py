a = str(input())
b = str(input())
c = str(input())
d = []
color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

value = [i for i in range(10)]
key = [10**i for i in range(10)]

d.append(color.index(a))
d.append(color.index(b))
d.append(color.index(c))

u = str(value[d[0]])+str(value[d[1]])
s = key[d[2]]
w = int(u)*s

print(w)