count, summ = map(int, input().split())
days = list(map(int, input().split()))

point = 0
res = 0

while summ:
    if summ - days[point] >= 0:
        summ -= days[point]
        res += 1
        if point != count - 1:
            point += 1
    else:
        if point == count - 1 or point:
            point = 0
            res += 1
        elif not point:
            break

print(-1 if summ else res)