n, x = map(int, input().split())
maks = -1e10
arr = [0] + list(map(int, input().split()))
dp = [0 for i in range(0, n + 1)]

for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], maks + arr[i] - x)
    maks = max(maks, dp[i - 1] - arr[i])

print(dp[n])
