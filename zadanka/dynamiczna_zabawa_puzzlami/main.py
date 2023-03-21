n = int(input())
p, w, d = [1], [0], [0]

MOD = 1e9+7
for i in range(1, n+1):
    p.append((p[i-1] + w[i-1] + d[i-1]) % MOD)
    w.append((p[i-1] + 2*d[i-2]) % MOD)
    d.append((p[i-1] + w[i-1]) % MOD)
    i += 1

print(int(p[n]))
