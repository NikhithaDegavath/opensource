x, y, z = map(int, input().split())
days = x * y;
time = z * 1440;
if(days <= time):
    print("YES")
else:
    print("NO")
