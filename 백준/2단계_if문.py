# 1330: 두 수 비교하기
a, b = map(int, input().split(" "))
if a > b :
    print(">")
elif a < b :
    print("<")
else :
    print("==")


# 9498: 시험 성적
num = int(input())
# num = range(0, 101)
if 90 <= num <= 100 :
    print("A") 
elif 80 <= num <= 89 :
    print("B")
elif 70 <= num <= 79 :
    print("C")
elif 60 <= num <= 69 :
    print("D")
elif 0 <= num <= 59 :
    print("F")


# 2753: 윤년
year = int(input())
if year % 4 == 0 :
    if year % 100 != 0 :
        print("1")
    elif year % 400 == 0 :
        print("1")
    else :
        print("0")
else :
    print("0")


# 14681: 사분면 고르기
x_coordinate = int(input())
y_coordinate = int(input())
if x_coordinate > 0 and y_coordinate > 0 :
    print(1) 
elif x_coordinate < 0 and y_coordinate > 0 :
    print(2) 
elif x_coordinate < 0 and y_coordinate < 0 :
    print(3) 
elif x_coordinate > 0 and y_coordinate < 0 :
    print(4)


# 2884: 알람 시계
H, M = map(int, input().split(" "))
if 0 <= H <= 23 and 0 <= M <= 59 :
    if M >= 45 :
        print(H, M - 45)
    elif 0 <= M < 45 :
        if 0 < H <= 23 :
            print(H - 1, 60 + (M - 45))
        elif H == 0 :
            print(H + 23, 60 + (M - 45))


# 2525: 오븐 시계
A, B = map(int, input().split(" "))
C = int(input())
while True:
    if B + C >= 60:
        A += 1
        if A == 24:
            A = 0
        C -= (60 - B)
        B = 0
        if C == 0:
            print(A, B)
            break
    else:
        B += C
        C = 0
        print(A, B)
        break


# 2480: 주사위 세개
D1, D2, D3 = map(int, input().split(" "))
money = 0
    # 규칙 1번
if D1 == D2 == D3:
    money += 10000 + D1 * 1000
    # 규칙 2번
elif D1 == D2:
    money += 1000 + D1 * 100
elif D2 == D3:
    money += 1000 + D2 * 100
elif D1 == D3:
    money += 1000 + D3 * 100
    # 규칙 3번
elif D1 != D2 != D3:
    dice_max = max([D1, D2, D3])
    money += dice_max * 100
print(money)

