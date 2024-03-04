n = int(input())
arr = [0] * 123
for i in range(n):
    for j in input():
        if j.isupper():
            arr[ord(j)] += 1
        elif j.islower():
            arr[ord(j)] += 1

for i in range(97, 123):
    if arr[i] != 0: print(chr(i), arr[i])

for i in range(65, 91):
    if arr[i] != 0: print(chr(i), arr[i])