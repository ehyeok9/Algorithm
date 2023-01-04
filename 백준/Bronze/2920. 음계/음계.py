n = list(map(int, input().split()))

sorting = sorted(n)
resorting = list(reversed(sorting))

if n == sorting:
    print("ascending")
elif n == resorting:
    print("descending")
else:
    print("mixed")