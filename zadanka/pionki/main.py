n, m = map(int, input().split())
tab = [input().strip() for _ in range(n)]

w, ww, wiersz, kolumna, kk, ile = 0, 0, 0, 0, 0, 0
k = [0 for _ in range(m)]

for i in range(n):
    w = 0
    for j in range(m):
        if tab[i][j] == '#':
            w += 1
            k[j] += 1
            ile += 1
    if w > ww:
        ww = w
        wiersz = i

for i in range(m):
    if k[i] > kk:
        kk = k[i]
        kolumna = i

kk = max(k)
wynik = ww + kk

if tab[wiersz][kolumna] == "#":
    wynik -= 2
    ile -= 1

wynik += 2 * (ile - wynik)
print(wynik)
