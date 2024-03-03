n = int(input())
arr = list(map(int, input().split()))

max_value = max(arr)

print(''.join(chr(i + 65) for i, x in enumerate(arr) if x == max_value))