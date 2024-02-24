a = input()
res = ''

res += 'T' if (a.count('O') >= 1 and a.count('I') >= 1 and a.count('J') >= 1) else 'N'
res += 'T' if (a.count('O') >= 1 and a.count('I') >= 1 and a.count('J') >= 1 and a.count('E') >= 1) else 'N'
res += 'T' if (a.count('O') >= 1 and a.count('I') >= 2) else 'N'

print(res)
