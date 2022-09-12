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