n = int(input())
arr = list(map(int, input().split()))

arr.sort()
arr.reverse()

if (n < 4):
    print(0)
else: 
    print(arr[3] * arr[3])