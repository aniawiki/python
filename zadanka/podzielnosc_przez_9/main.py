def change_number(n):
    previous = n - n % 9
    next_num = n + (9 - n % 9)
    if n % 9 == 0:
        return n
    elif next_num // 10 == n // 10:
        return next_num
    else:
        return previous

n = int(input())
result = change_number(n)
print(result)
