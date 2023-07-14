def find_start_day(dif: int, n: int):
    days = 1
    while True:
        count_s, size_s = days - (n % days), n // days
        count_l, size_l = n % days, n // days + 1
        sum_arif_prog = ((size_s / 2) * (size_s - 1)) * count_s + ((size_l / 2) * (size_l - 1)) * count_l

        if sum_arif_prog <= dif:
            return days

        days += 1


def find_count_days(start_day: int):
    if start_day == 1:
        return 1

    quotes.sort(reverse=True)

    flag = True
    for i in range(start_day - 1, 0, -1):
        tmp = target

        for k in range(i):
            for dif, effect in enumerate(quotes[k::i]):
                if effect - dif <= 0:
                    break

                tmp -= effect - dif
                dif += 1

                if tmp <= 0:
                    flag = True
                    break

        if tmp > 0 and flag:
            return i + 1

    return 1


count, target = map(int, input().split())
quotes = list(map(int, input().split()))

sum_quotes = sum(quotes)

if sum_quotes < target:
    print(-1)
elif sum_quotes == target:
    print(count)
else:
    print(find_count_days(find_start_day(sum_quotes - target, count)))
