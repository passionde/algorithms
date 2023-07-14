three = {}
count = int(input())

for i in range(1, count+1):
    three[i] = {"nodes": [], "boxs": 0}

for _ in range(count - 1):
    road = tuple(map(int, input().split()))
    u, v = min(road), max(road)

    three[u]["nodes"].append(v)

for _ in range(int(input())):
    u, k, x = map(int, input().split())

    three[u]["boxs"] += x
    queue = three[u]["nodes"]
    while k > 0 and queue:
        print("hi")
        tmp = []
        for city in queue:
            three[city]["boxs"] += x
            tmp.extend(three[city]["nodes"])

        queue = tmp
        k -= 1

for city in three.values():
    print(city["boxs"], end=" ")