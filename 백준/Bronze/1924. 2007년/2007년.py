month, day = map(int, input().split())

days = 0

month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(month):
    days += month_day[i]

days += day-1

yoyil = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

print(yoyil[days%7])