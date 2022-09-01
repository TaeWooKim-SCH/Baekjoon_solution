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


# 14425: 문자열 집합
import sys
N, M = map(int, sys.stdin.readline().split())
N_set = set()
M_list = []
score = 0
for i in range(N): 
    S = sys.stdin.readline()
    N_set.add(S)
for i in range(M):
    M_string = sys.stdin.readline()
    M_list.append(M_string)
for i in range(M):
    if M_list[i] in N_set:
        score += 1
print(score)


# 1620: 나는야 포켓몬 마스터 이다솜





