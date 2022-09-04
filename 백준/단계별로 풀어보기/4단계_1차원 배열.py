# 10818: 최소, 최대
N = int(input())
num = list(map(int, input().split(" ")))
num_sol = sorted(num)
print(num_sol[0], num_sol[-1])
print(min(num), max(num)) # 이게 더 빠른 시간


# 2562: 최댓값
N_list = []
for i in range(9):
    N = int(input())
    N_list += [N]
N_max = max(N_list)
print(N_max)
print(N_list.index(N_max) + 1)


# 2577: 숫자의 개수
n = 1
for i in range(3):
    N = int(input())
    n *= N
print(str(n).count('0'))
print(str(n).count('1'))
print(str(n).count('2'))
print(str(n).count('3'))
print(str(n).count('4'))
print(str(n).count('5'))
print(str(n).count('6'))
print(str(n).count('7'))
print(str(n).count('8'))
print(str(n).count('9'))


# 3052: 나머지
N_list = []
for i in range(10):
    N = int(input())
    num = N % 42
    N_list += [num]
N_list = set(N_list)
print(len(N_list))


# 1546: 평균
N = int(input())
M = list(map(int, input().split(" ")))
M_max = max(M)
new_M = []
for i in M:
    new_M += [i / M_max * 100]
print(sum(new_M) / len(new_M))


# 8958: OX퀴즈
T = int(input())
for i in range(T):
    result = input()
    grade = 0
    score = 0
    for x in result:
        if x == "O":
            score += 1
            grade += score
        else:
            score = 0
    print(grade)


# 4344: 평균은 넘겠지
C = int(input())
per = [] # 한 번에 정답을 출력하기 위한 리스트
for i in range(C):
    N_score = list(map(int, input().split(" "))) # 학생수와 점수 입력
    arange = sum(N_score[1:]) / N_score[0] # 평균 구하기
    winner = [] # 평균보다 높은 학생들의 리스트
    for x in N_score[1:]: # 평균보다 높은 학생들을 구하는 반복문
        if x > arange:
            winner += [x]
    per += [format(len(winner) / (len(N_score) - 1) * 100, ".3f") + "%"] # 평균보다 높은 학생들의 비율
for j in per: # 반복문을 이용하여 한 번에 출력
    print(j)
