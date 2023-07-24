b = 0
score = 0
c = 0
arr1=[]
arr2=[]
n, str1, str2 = int(input()), input(), input()
if (str1.count('B') < n / 2): b = 1

if (b == 0):
    for i in range(n):
        if (str1[i] == 'C'):
            arr1.append(i)
            c += 1
        if (str2[i] == 'B'): arr2.append(i)
if (b == 1):
    for i in range(n):
        if (str1[i] == 'B'): arr1.append(i)
        if (str2[i] == 'C'):
            arr2.append(i)
            c += 1

for i in range(c): score += abs(arr1[i] - arr2[i]) + 1
print(score)