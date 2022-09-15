# 5086: 배수와 약수
import sys
while True:
    first, second = map(int, sys.stdin.readline().split())
    if first == 0 and second == 0:
        break
    else:
        if second % first == 0:
            print("factor")
        elif first % second == 0:
            print("multiple")
        else:
            print("neither")


# 1037: 약수
import sys
N_count = int(sys.stdin.readline())
N_set = sorted(map(int, sys.stdin.readline().split())) # 오름차순 정렬
if N_count == 1: # 제곱수일 때
    print(N_set[0] ** 2)
else: # 그 외 전부
    print(N_set[0] * N_set[-1])


# 2609: 최대공약수와 최소공배수
import sys
a, b = map(int, sys.stdin.readline().split())
gcf = 1 # 최대공약수
lcm = 1 # 최소공배수
small_num = [] # 소인수들의 리스트
i = 2 # 소인수
while i <= a or i <= b:
    if a % i == 0 and b % i == 0: # 둘 다 나누어 떨어지면 소인수
        a = a // i
        b = b // i
        small_num.append(i)
    else: # 안 나누어 떨어지면 다음 수로 넘어감
        i += 1
small_num.append(a) # 최종 소인수
small_num.append(b) # 최종 소인수
if len(small_num) == 2: # a와 b가 서로소일 때
    print(1) # 최대공약수
    print(a * b) # 최소공배수
else: # 아닐 때
    for i in range(len(small_num) - 2): 
        gcf *= small_num[i]
    for i in range(len(small_num)):
        lcm *= small_num[i]
    print(gcf)
    print(lcm)


# 1934: 최소공배수
#     # 방법1: 실패
# import sys
# T = int(sys.stdin.readline())
# for i in range(T):
#     A, B = map(int, sys.stdin.readline().split())
#     small_num = []
#     i = 2
#     while i <= A or i <= B:
#         if A % i == 0  and B % i == 0:
#             A = A // i
#             B = B // i
#             small_num.append(i)
#         else:
#             i += 1
#     small_num.append(A)
#     small_num.append(B)
#     if len(small_num) <= 2:
#         print(A * B)
#     else:
#         a = 1
#         for i in small_num:
#             a *= i
#         print(a)
    # 방법2: 유클리드 호제법
        # 큰 수를 작은 수로 나누어 구한 나머지로 큰 수를 대체한다. 
        # 큰 수를 작은 수로 계속 나누어서, 나누어 떨어질 때까지 반복한다.
        # 나누어 떨어질 때(나머지가 0일 때), 나누는 수가 최대공약수이다.
import sys
T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    if A > B:
        A, B = B, A
    C ,D = A, B # 나중에 A와 B가 바뀌게 됨을 대비한 값 저장
    while B > 0:
        A = A % B
        A, B = B, A
    gcf = A
    print(C * D // gcf)

