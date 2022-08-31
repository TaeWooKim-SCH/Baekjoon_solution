# 10815: 숫자카드
import sys
N = int(sys.stdin.readline())
N_set = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    if M_list[i] in N_set:
        print(1)
    else:
        print(0)





