n, x, y = map(int, input().split())
marks = n * x;
if(y>marks or y % x != 0 or y // x>n):
    print("NO")
else:
    print("YES")
