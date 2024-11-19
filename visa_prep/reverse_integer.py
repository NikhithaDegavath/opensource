n = int(input())
r1, r2 = -2**31, 2**31 - 1
neg = n < 0
if neg:
    n = -n
r_num = int(str(n)[::-1])
if neg:
    r_num = -r_num
if r_num < r1 or r_num > r2:
    print(0)
else:
    print(r_num)
