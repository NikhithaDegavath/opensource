n = int(input())
curr_num = 1;
for i in range(1, n + 1):
    row_num = [str(curr_num + j) for j in range(i)]
    print(" ".join(row_num))
    curr_num = curr_num + i
