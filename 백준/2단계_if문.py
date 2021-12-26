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

