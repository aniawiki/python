n = int(input())
score = 0

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort(reverse=True)

for i in range(n):
    score += pow(10, len(str(arr2[i]))) * arr1[i] + arr2[i]
print(score)
