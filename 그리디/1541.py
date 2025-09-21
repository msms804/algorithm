import sys

sums = []
# 1. -를 기준으로 나누기
expr = sys.stdin.readline().strip()

parts = expr.split('-')

for part in parts:
    tokens = part.split('+')
    numbers = list(map(int, tokens))
    total = sum(numbers)
    sums.append(total)

ret = sums[0]
for value in sums[1: ]:
    ret -= value

print(ret)