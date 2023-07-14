def clear_dataset_gen(values: list, counts):
    idx = 1
    count = counts[0]
    while idx < len(values):
        if values[idx - 1] == values[idx]:
            count += counts[idx]
        else:
            yield [values[idx - 1], count]
            count = counts[idx]
        idx += 1
    yield [values[-1], count]


def gen_par(gen_1, gen_2):
    set_1, set_2 = next(gen_1), next(gen_2)
    while set_2[1] != 0 and set_1[1] != 0:
        tmp_min = min(set_1[1], set_2[1])
        yield (set_1[0], tmp_min), (set_2[0], tmp_min)

        set_1[1] -= tmp_min
        set_2[1] -= tmp_min

        try:
            if set_1[1] == 0:
                set_1 = next(gen_1)
        except StopIteration:
            pass

        try:
            if set_2[1] == 0:
                set_2 = next(gen_2)
        except StopIteration:
            pass


input()
val1, count1 = input().split(), tuple(map(int, input().split()))
input()
val2, count2 = input().split(), tuple(map(int, input().split()))

pos = 1
count = 0
for set_1, set_2 in gen_par(clear_dataset_gen(val1, count1), clear_dataset_gen(val2, count2)):
    if set_1[0] != set_2[0]:
        count += ((pos + pos + set_1[1] - 1) / 2) * set_1[1]
    pos += set_1[1]

print(int(count))