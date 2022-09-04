# 1978: 소수 찾기
N = int(input())
num = set(map(int, input().split(" ")))
no_prime = set()
if 1 in num:
    no_prime.update({1})
for i in num:
    for x in range(2, 40): # 11이상의 제곱수 때문에 여기까지 해줘야 함
        if i > x: # 2 / 2같은 연산 때문에 이 조건을 추가해줘야 함
            if i % x == 0: # 
                no_prime.update({i})
print(len(num - no_prime))


# 2581: 소수
M = int(input())
N = int(input())
num = set() # M 이상 N 이하의 자연수를 넣기 위한 변수
no_prime = set() # num에서 소수가 아닌 수를 빼면 소수만 나옴
for i in range(M, N + 1): # M이상 N이하 자연수를 넣는 반복문
    num.update({i})
if 1 in num: # 1은 소수에서 제외
    no_prime.update({1})
for x in num: # 소수가 아닌 수들을 찾기 위한 반복문
    for j in range(2, 100): # 중복되어서 들어가는 게 생기기 때문에 집합을 이용
        if x > j: # x보다 j가 크게 되면 무조건 나머지가 0이 안나오기 때문에 이 조건 필요
            if x % j == 0:
                no_prime.update({x})
prime_num = set(num - no_prime)
if len(prime_num) == 0:
    print(-1)
else:
    print(sum(prime_num))
    print(min(prime_num))


# 11653: 소인수분해
N = int(input())
for i in range(2, N + 1): 
    while N % i == 0: # i는 순서대로 들어가기 때문에 안 나눠지기 전까지 i를 출력함
        print(i)
        N = N // i


# 1929: 소수 구하기
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False
    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
M, N = map(int, input().split(" "))
for k in prime_list(N + 1):
    if k >= M:
        print(k)


# 4948: 베르트랑 공준
def prime_list(n): # 에라토스테네스의 체
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for x in range(i + i, n, i):
                sieve[x] = False
    return [i for i in range(2, n) if sieve[i] == True]
prime_len = []
while True:
    n = int(input())
    if n == 0:
        break
    prime_len += [len(set(prime_list(2 * n + 1)) - set(prime_list(n + 1)))]
for k in prime_len:
    if k != 0:
        print(k)

    
# 9020: 골드바흐의 추측
    # 에라토스테네스의 체
MAX = 10_001
sieve = [True] * MAX
for i in range(2, MAX):
    if sieve[i] == True:
        for x in range(i*2, MAX, i):
            sieve[x] = False
    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
TEST_CASE = int(input())
for j in range(TEST_CASE):
    n = int(input()) # 데이터 받기
    number_distance = MAX # 정답 찾기위한 숫자 2개 거리 비교 저장
    answer = (0, 0) # 정답 저장 공간
    for i in range(1, (n//2) + 1):
        # <  (n//2) + 1 # 10이 들어온다고 하면 5까지 비교해야함
        # 10 까지 갈필요 없음(시간 단축)
        if sieve[i] == True and sieve[n - i] == True: # 둘다 소수 인지 확인
            if number_distance > (tmp := abs((n - i) - i)): # tmp := abs((n - i) - i) < 의미 : abs((n - i) - i)값 tmp에 저장
                # 정답 찾는  if 문 2개의 수 거리 비교
                answer = (n - i, i) # 정답 저장
                number_distance = tmp
    answer = sorted(answer) # 낮은 수가 앞으로 정렬
    print(answer[0], answer[1]) # 정답 출력
        
            










