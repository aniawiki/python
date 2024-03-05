n = int(input())
arr = [None] * n
for i in range(n):
    a = input()
    arr[i] = (len(a), a)
arr.sort()

for i in arr:
    print(i[1])