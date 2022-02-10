# 2798: 블랙잭
def black_jack(n, m):
    # n: 카드의 개수
    # m: 딜러가 부른 숫자
    card_num = list(map(int, input().split(" ")))
    card_sum = set() # 카드 세 개의 합들의 집합    
    for i in card_num:
        for x in card_num:
            if i != x: # 이미 카드 한 장을 뽑았기 때문에 뽑은 카드는 제외시켜야 함
                for j in card_num:
                    if (j != x) and (j != i): # 두 개의 카드 제외
                        if i + x + j <= m: # 딜러가 부른 숫자보다 작을 때
                            card_sum.update({i + x + j}) # 추가
    print(max(card_sum))
N, M = map(int, input().split(" "))
black_jack(N, M)

    # 모듈 이용하기
from itertools import combinations
N, M = map(int, input().split(" "))
print(max({a + b + c for a, b, c in combinations(list(map(int, input().split(" "))), 3) if a + b + c <= M}))



# 2231: 분해합
def const(n):
    constructor_list = [] # 생성자들의 리스트
    for i in range(1, n): # n까지 값들 비교
        num = i # 각 자리 숫자들을 더하기 위해 값을 저장
        for x in range(len(str(i))):
            num += int(str(i)[x]) # 각 자리 숫자들을 원래 숫자에 더함
        if num == n: # 만약 위에서 더한 값과 n이 같으면 
            constructor_list += [i] # 생성자이므로 추가
    if len(constructor_list) >= 1: # 생성자가 1개라도 존재하면
        print(min(constructor_list)) # 최솟값 출력
    else: # 없으면
        print(0) # 0 출력
N = int(input())
const(N)



# 7568: 덩치
def bigbody(n):
    # n: 덩치들의 수
    body_list = [list(map(int, input().split(" "))) for _ in range(n)] # 각각의 덩치들을 몸무게와 키 순서대로 리스트를 만들어줌
    for x, y in body_list: # 기준이 되는 덩치
        rank = 1 # 순위
        for p, q in body_list: # 비교되는 덩치
            if x < p and y < q: # 기준이 되는 덩치보다 비교되는 덩치가 더 크다면
                rank += 1 # 순위 + 1
        print(rank, end = " ")
N = int(input())
bigbody(N)



# 1018: 체스판 다시 칠하기
N, M = map(int, input().split(" "))
chess_board = [] # 체스판
count = [] # 수정해야 할 횟수들의 리스트
for _ in range(N):
    chess_board.append(input())
for a in range(N - 7): # 8 x 8로 자를 수 있는 범위의 시작점을 가리킴
    for b in range(M - 7): # 8 x 8로 자를 수 있는 범위의 시작점을 가리킴
        start_W = 0 # 'W'로 시작할 경우 바뀐 체스 판의 갯수를 세기 위함
        start_B = 0 # 'B'로 시작할 경우 바뀐 체스 판의 갯수를 세기 위함
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0: # 현재 행의 번호(i)와 현재 열의 번호(j)의 합이 짝수이면 시작점의 색깔과 같아야 함
                    if chess_board[i][j] != "W": # 짝수이기 때문에 'W'여야 하는데 'W'가 아니라면
                        start_W += 1 # index1에 1을 더함
                    if chess_board[i][j] != "B": # 짝수이기 때문에 'B'여야 하는데 'B'가 아니라면
                        start_B += 1 # index2에 1을 더함
                else: # 현재 행의 번호(i)와 현재 열의 번호(j)의 합이 홀수이면 시작점의 색깔과 달라야 함
                    if chess_board[i][j] != 'B': # 홀수이기 때문에 'B'여야 하는데 'B'가 아니라면
                        start_W += 1 # index1에 1을 더함
                    if chess_board[i][j] != 'W': # 홀수이기 때문에 'W'여야 하는데 'W'가 아니라면
                        start_B += 1 # index2에 1을 더함
        count.append(min(start_W, start_B)) # index1과 index2중에서 더 작은 값을 count에 추가
print(min(count)) # 최종적으로 가장 작은 값을 출력                



# 1436: 영화감독 숌
def title(n):
    nums = set() # 집합으로 계산시간 단축하기 위해 만듦
    for i in range(666, 10000000): # 전체 경우의 수를 추가함
        if '666' in str(i):
            nums.update({i})
    print(sorted(nums)[n - 1])
N = int(input())
title(N)
