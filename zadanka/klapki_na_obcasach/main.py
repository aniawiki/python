n = int(input())
heights = list(map(int, input().split()))
m = int(input())
heels = list(map(int, input().split()))
t = int(input())

heights.sort()
heels.sort(reverse=True)

score = 0
for i in range(n):
    if (heights[i] >= t):
        heights[i] = -1
        score += 1

j = 0
i = 0
while (i < n and j < m):
    if (heights[i] >= 0 and heights[i] + heels[j] >= t):
        j += 1
        score += 1
    i += 1

print(score)
