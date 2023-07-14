def gen_seq(count_place: int):
    while True:
        left = count_place // 2
        right = count_place // 2 + 1

        flag = count_place % 2

        for _ in range(count_place):
            flag = not flag
            if flag:
                left -= 1
                yield left + 1
            else:
                right += 1
                yield right - 1


n, m = map(int, input().split())
seq = gen_seq(m)

for i in range(n):
    print(next(seq))

