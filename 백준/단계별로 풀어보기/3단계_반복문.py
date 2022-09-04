# 2739: 구구단
num = int(input())
for x in range(1, 10) :
    a = x * num
    print(str(num), "*", str(x), "=", str(a))


# 10950: A + B - 3
num = int(input())
for x in range(num) :
    A, B = map(int,input().split(" "))
    print(A + B)


# 8393: 합
num = int(input())
y = 0
for x in range(0, num + 1) :
    y += x
print(y)


# 25304: 영수증
X = int(input())
N = int(input())
thing_list = []
sum = 0
for i in range(N):
     thing_list.append(list(map(int, input().split())))
for a, b in thing_list:
    sum += a * b
if sum == X:
    print("Yes")
else:
    print("No")


# 15552: 빠른 A + B
import sys
T = int(sys.stdin.readline())
for x in range(T) :
    A, B = map(int, sys.stdin.readline().split(" "))
    print(A + B)


# 2741: N 찍기
N = int(input())
for x in range(1, N + 1) :
    print(x)


# 2742: 기찍 N
N = int(input())
for x in reversed(range(1, N + 1)):
    print(x)


# 11021: A + B - 7
T = int(input())
for x in range(1, T + 1) :
    A, B = map(int, input().split(" "))
    print("Case #" + str(x) + ":", A + B)


# 11022: A + B - 8
T = int(input())
for x in range(1, T + 1) :
    A, B = map(int, input().split(" "))
    print("Case #" + str(x) + ":", str(A), "+", str(B), "=", A + B)


# 2438: 별 찍기 - 1
N = int(input())
for x in range(1, N + 1) :
    print("*" * x)


# 2439: 별 찍기 - 2
N = int(input())
for x in range(1, N + 1) :
    print("{:>{}}".format("*" * x, N))


# 10871: X보다 작은 수
N, X = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
for i in A:
    if i < X:
        print(i, end = " ")


# 10952: A + B - 5
while True :
    A, B = map(int, input().split(" "))
    if A == 0 and B == 0 :
        break
    else :
        print(A + B)


# 10951: A + B - 4
while True :
    try :
        A, B = map(int, input().split((" ")))
        print(A + B)
    except :
        break


# 1110: 더하기 사이클
N = int(input())
N_t = N
re = 0 # 반복문 횟수
while True:
    re += 1
    # 주어진 숫자가 10보다 작을때
    if N < 10:
        N = "0" + str(N)
        N = int(N[-1] + str(int(N[0] + N[1])))
    # 주어진 숫자가 10보다 크거나 같을 때
    else:
        N = str(N)
        N = int(N[-1] + str(int(N[0]) + int(N[1]))[-1])
    # 멈추기
    if N == N_t:
        break
print(re)