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