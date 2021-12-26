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
