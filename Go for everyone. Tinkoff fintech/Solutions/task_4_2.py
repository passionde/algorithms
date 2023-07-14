def find_start_day(dif: int, n: int):
    # Определяет стартовый день на основе арифметической прогрессии
    # Но не учитывает, что число может быть меньше значения члена прогрессии
    # Поэтому нуждается в дополнительной проверке
    days = 1
    while True:
        # Количество блоков с min количеством элементов, само количество
        count_s, size_s = days - (n % days), n // days
        # Количество блоков с min + 1 количеством элементов, само количество + 1
        count_l, size_l = n % days, n // days + 1
        # Сумма прогрессии такой комбинации
        sum_arif_prog = ((size_s / 2) * (size_s - 1)) * count_s + ((size_l / 2) * (size_l - 1)) * count_l

        if sum_arif_prog <= dif or days == n:
            # print(count_s, size_s)
            # print(count_l, size_l)
            # print(sum_arif_prog, days, n)
            return days

        days += 1


def find_count_days(start_day):
    if start_day == 1:
        return 1

    quotes.sort(reverse=True)
    flag = True
    for i in range(start_day - 1, 0, -1):
        tmp = target
        for day in parting_gen(quotes, i):
            print(day)
            dif = 0
            for effect in day:
                if effect - dif <= 0:
                    break

                tmp -= effect - dif
                dif += 1

                if tmp <= 0:
                    flag = True
                    break

        if tmp > 0 and flag:
            return i + 1


def parting_gen(xs, parts):
    for i in range(parts):
        yield xs[i::parts]


count, target = map(int, input().split())
quotes = list(map(int, input().split()))

sum_quotes = sum(quotes)
count = len(quotes)

if sum_quotes < target:
    print(-1)
elif sum_quotes == target:
    print(count)
else:
    print(find_count_days(find_start_day(sum_quotes - target, count)))
