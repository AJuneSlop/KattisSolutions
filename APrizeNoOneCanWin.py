n, limit = [int(x) for x in input().split()]
items = sorted([int(x) for x in input().split()])

for i in range(1, n):
    if items[i] + items[i - 1] > limit:
        n = i
        break
print(n)
