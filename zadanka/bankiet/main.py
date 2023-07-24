n = int(input())
i = 0
j = 1
tables = 0
arr = []
arr.append(0)


visited = []
for i in range (n+3):
    visited.append(False)

for i in range(n):
    x = int(input())
    arr.append(x)

i = 1
while i <= n:
    if (visited[i] == False):
        visited[i] = True
        tables += 1
        j = arr[i]
        while j != i:
            visited[j] = True
            j = arr[j]
    i += 1

print(tables)