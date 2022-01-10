# 1712: 손익분기점
A, B, C = map(int, input().split(" "))

if C > B :
    sale_num = A // (C - B)
    print(sale_num + 1)
else :
    print(-1)


# 2292: 벌집
N = int(input())
a, b, i = 2, 7, 0
if N == 1 :
    print(1)
else :
    for i in range(1000000000) :
        if a <= N <= b :
            print(i + 2)
            break
        else :
            a += 6 * (i + 1)
            b += 6 * (i + 2)


# 1193: 분수찾기
X = int(input())
line = 0 # 사선 라인
max_num = 0 # 입력된 숫자(X 변수)의 라인에서 가장 큰 숫자
while X > max_num:
    line += 1
    max_num += line
    # print('line:', line)
    # print('max_num:', max_num)
gap = max_num - X 
# print("gap:", gap)
if line % 2 == 0: # 사선 라인이 짝수번째 일 때
    top = line - gap # 분자
    under = gap + 1 # 분모
else: # 사선 라인이 홀수 번째 일 때
    top = gap + 1 # 분자
    under = line - gap # 분모
print(f'{top}/{under}')


# 2869: 달팽이는 올라가고 싶다
a, b, v = map(int, input().split(" "))

d = (v - a) / (a - b)

if d == int(d) :
    print(int(d) + 1)
else :
    print(int(d) + 2)

            
# 10250: ACM 호텔
import sys

n = int(sys.stdin.readline())

for i in range(n) :
    H, W, N = map(int, sys.stdin.readline().split(" "))
    for x in range(1, W + 1) :
            if H * (x - 1) < N <= H * (x):
                if N % H != 0 :
                    room_number = str(N % H) + str((N // H) + 1).zfill(2)
                else :
                    room_number = str(H) + str((N // H)).zfill(2)

                print(int(room_number))


# 2775: 부녀회장이 될테야
import sys

def apart(a, b) :
    resident_number = 0
    if a == 0 :
        return b
    elif b == 1 :
        return b
    else :
        resident_number += apart(a - 1, b)
        resident_number += apart(a, b - 1)
        return resident_number

T = int(sys.stdin.readline())
for x in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    if 1 <= k <= 14 :
        if 1 <= n <= 14 :
            print(apart(k, n))


# 2839: 설탕 배달
N = int(input())
bag = 0
while N >= 0:
    if N % 5 == 0: # 5의 배수이면
        bag += (N // 5) # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    N -= 3
    bag += 1 # 5의 배수가 될 때까지 설탕 -3, 봉지 +1
else:
    print(-1)


# 10757: 큰 수 A + B
A, B = map(int, input().split(" "))
print(A + B)    
    

# 1011: Fly me to the Alpha Centauri
T = int(input()) # 규칙찾기!!!!!!!!    이동 횟수가 짝수가 될 때마다 이동 횟수가 늘어남
for _ in range(T):
    x, y = map(int, input().split(" "))
    dis = y - x
    count = 0 # 이동 횟수
    move = 1 # count별 이동 가능한 거리
    move_plus = 0 # 이동한 거리의 합
    while move_plus < dis:
        count += 1
        move_plus += move # count 수에 해당하는 move를 더함
        if count % 2 == 0: # count가 2의 배수일 때
            move += 1
    print(count)
