x, y, z = map(int, input().split())
weight = z - y
if (weight < 0):
    print(0)
else:
    maximum = weight // x
    print(maximum)
