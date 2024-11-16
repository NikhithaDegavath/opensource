x, n = map(int, input().split());
c = x*100;
if c >= n:
    print(0)
else:
    r = n - c;
    n_p = (r + 100 - 1) // 100
    print(n_p)
