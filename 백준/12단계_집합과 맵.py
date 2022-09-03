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
import sys
N, M = map(int, sys.stdin.readline().split())
N_dict = dict()
reverse_dict = dict()
for i in range(N):
    poketmon_name = sys.stdin.readline().strip()
    N_dict.update({poketmon_name: i + 1})
    reverse_dict.update({i + 1: poketmon_name})
for i in range(M):
    question = sys.stdin.readline().strip()
    if N_dict.get(question) == None:
        print(reverse_dict[int(question)])
    else:
        print(N_dict[question])


# 10816: 숫자 카드 2
import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
N_dict = dict()
for i in N_list:
    if i in N_dict:
        N_dict[i] += 1
    else: 
        N_dict[i] = 1
for i in M_list:
    if N_dict.get(i) == None:
        print(0)
    else:
        print(N_dict[i])

