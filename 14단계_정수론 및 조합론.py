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
        