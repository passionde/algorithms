def find_count_days():
    quotes.sort(reverse=True)
    for i in range(1, count):
        tmp = target
        for day in parting_gen(quotes, i):
            dif = 0
            for effect in day:
                if effect - dif <= 0:
                    break

                tmp -= effect - dif
                dif += 1
                if tmp <= 0:
                    return i


def parting_gen(xs, parts):
    for i in range(parts):
        yield xs[i::parts]


count, target = map(int, input().split())
quotes = list(map(int, input().split()))
sum_quotes = sum(quotes)

if sum_quotes < target:
    print(-1)
elif sum_quotes == target:
    print(count)
else:
    print(find_count_days())
