t = int(input())
for _ in range(t):
    x, n = map(int, input().split())
    p = x // 10
    s = p * n
    print(s)