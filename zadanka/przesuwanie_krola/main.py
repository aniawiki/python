start = input()
finish = input()

y1, x1 = ord(start[0]) - 96, int(start[1])
y2, x2 = ord(finish[0]) - 96, int(finish[1])

res = ""
minn = min(abs(x2 - x1), abs(y2 - y1))

if (x1 < x2 and y1 < y2):
    res += "NE " * minn
    x1 += minn
    y1 += minn
elif (x1 < x2 and y1 > y2):
    res += "NW " * minn
    x1 += minn
    y1 -= minn
elif (x1 > x2 and y1 < y2):
    res += "SE " * minn
    x1 -= minn
    y1 += minn
elif (x1 > x2 and y1 > y2):
    res += "SW " * minn
    x1 -= minn
    y1 -= minn

if (x1 < x2): res += "N " * (x2 - x1)
elif (x1 > x2): res += "S " * (x1 - x2)
elif (y1 < y2): res += "E " * (y2 - y1)
elif (y1 > y2): res += "W " * (y1 - y2)
print(res.strip().count(" ") + 1)
print(res)