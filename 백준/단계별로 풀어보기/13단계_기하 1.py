# 1085: 직사각형에서 탈출
x, y, w, h = map(int, input().split(" "))
print(min([x, y, w - x, h - y]))


# 3009: 네 번째 점
x1, y1 = map(int, input().split(" "))
x2, y2 = map(int, input().split(" "))
x3, y3 = map(int, input().split(" "))
x_list = [x1, x2, x3] # x 좌표들의 리스트
y_list = [y1, y2, y3] # y 좌표들의 리스트
x = 0
y = 0
for i in set(x_list):
    if x_list.count(i) == 1:
        x += i
for j in set(y_list):
    if y_list.count(j) == 1:
        y += j
print(x, y)


# 4153: 직각삼각형
answer = []
while True:
    a, b, c = map(int, input().split(" "))
    if (a and b and c) == 0:
        break
    else:
        abc_list = [a, b, c]
        abc_max = max(abc_list)
        abc_list.remove(abc_max)
        if abc_max ** 2 == abc_list[0] ** 2 + abc_list[1] ** 2:
            answer += ["right"]
        else:
            answer += ["wrong"]
for i in answer:
    print(i)


# 2477: 참외밭
import sys
K = int(sys.stdin.readline())
filed_dict = dict()
vertical_list = [] # 세로 방향 리스트
width_list = [] # 가로 방향 리스트
direc_list = [] # 방향, 길이 리스트
inside = 0 # 빼야할 면적

for i in range(6):
    direc, length = map(int, sys.stdin.readline().split())
    direc_list.append([direc, length])

    # 바깥 부분 면적
    if (direc == 3) or (direc == 4):
        vertical_list.append(length)
    elif (direc == 1) or (direc == 2):
        width_list.append(length)

# 안쪽 부분 면적(2-4, 3-2, 1-3, 4-1)
for i in range(5):
    if direc_list[i][0] == 1:
        if direc_list[i + 1][0] == 3:
            inside = direc_list[i][1] * direc_list[i + 1][1]
    elif direc_list[i][0] == 2:
        if direc_list[i + 1][0] == 4:
            inside = direc_list[i][1] * direc_list[i + 1][1]
    elif direc_list[i][0] == 3:
        if direc_list[i + 1][0] == 2:
            inside = direc_list[i][1] * direc_list[i + 1][1]
    elif direc_list[i][0] == 4:
        if direc_list[i + 1][0] == 1:
            inside = direc_list[i][1] * direc_list[i + 1][1]

# 시작과 끝이 안쪽 면적일때        
if inside == 0: 
    inside = direc_list[0][1] * direc_list[-1][1]
            
outside = max(vertical_list) * max(width_list) # 밭의 바깥 부분 면적
print((outside - inside) * K)




# 3053: 택시 기하학
R = int(input())
print(round(3.14159265359 * (R ** 2), 6))
print(format(2.000000 * (R ** 2), ".6f"))


# 1002: 터렛
import math
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(" "))
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) # 두 점 사이의 거리
    if d == 0 and r1 == r2: # 두 원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r1 - r2) == d or r1 + r2 == d: # 내접, 외접일 때
        print(1)
    elif abs(r1 - r2) < d < r1 + r2: # 두 원이 서로 다른 두 점에서 만날 때
        print(2)
    else:
        print(0) # 그 외에
