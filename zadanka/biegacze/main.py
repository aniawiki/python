import math

a, b, c = list(map(int, input().split()))
print(c // int(a*b / math.gcd(a, b)))

# print((lambda a, b, c: str(c // (a * b // math.gcd(a, b))))(*map(int, input().split())))
