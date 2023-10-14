n = int(input())
tables = 0
arr = [0] + [int(input()) for _ in range(n)]
visited = [False] * (n+3)

for i in range(1, n + 1):
    if not visited[i]:
        visited[i] = 1
        tables += 1
        j = arr[i]
        while j != i:
            visited[j] = True
            j = arr[j]
    i += 1

print(tables)
