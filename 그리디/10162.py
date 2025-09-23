import sys

T = int(sys.stdin.readline())

if T % 10 != 0:
    print(-1)
    sys.exit()

times = [300, 60, 10]
counts = []

for time in times:
    count = T // time
    counts.append(count)
    T %= time

print(*counts)