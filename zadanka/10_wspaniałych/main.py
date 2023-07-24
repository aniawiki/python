n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)

print(' '.join(str(arr[i]) for i in range(10)))