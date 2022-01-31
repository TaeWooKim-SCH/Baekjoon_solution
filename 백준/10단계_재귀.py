# 10872: 팩토리얼
def fac(n):
    if n <= 1:
        return 1
    return n * fac(n - 1)
N = int(input())
print(fac(N))


# 10870: 피보나치 수 5
    # 재귀함수
def fibonachi(n):
    if n <= 1:
        return n
    return fibonachi(n - 1) + fibonachi(n - 2)
print(fibonachi(int(input())))
    # for문
N = int(input())
fibo_list = [0, 1]
for i in range(N - 1):
    fibo_list += [fibo_list[-1] + fibo_list[-2]]
if N == 0:
    print(0)
else:
    print(fibo_list[-1])


# 2447: 별 찍기 - 10
N = int(input()) # 입력받기
empty_star = [[' ' for _ in range(N)] for _ in range(N)] # 간단히 얘기하면 빈 공간을 만들어줌
def star(size, x, y):
    if size == 1: # 크기를 계속 3으로 나누다가 1이 되면
        empty_star[y][x] = '*' # 그 위치를 모두 별로 채움
    else: # 크기가 1이 아닐 때
        next_size = size // 3 # 크기를 3으로 나눈 몫
        for dy in range(3): # 3 x 3 의 정사각형 형태로 봐서 반복문을 만들어줌
            for dx in range(3):
                if dy != 1 or dx != 1: # 좌표가 (1, 1)이 아니라면
                    star(next_size, x + dx * next_size, y + dy * next_size)
star(N, 0, 0)
for i in empty_star:
    print(''.join(i))


# 11729: 하노이 탑 이동 순서
def hanoi(n, start, end, process):
    # n: 원반의 개수
    # start: 옮길 원반이 현재 있는 출발점 기둥
    # end: 원반을 옮길 도착점 기둥
    # process: 옮기는 과정에서 사용할 보조 기둥
    if n == 1: # 원반이 한 개일 땐 그냥 옮기면 됨
        print(start, end)
        return
    # 원반 n - 1개를 process로 이동(end를 보조 기둥으로)
    hanoi(n - 1, start, process, end)
    # 가장 큰 원반을 목적지로 이동
    print(start, end)
    # process에 있는 원반 n - 1개를 목적지로 이동(start를 보조 기둥으로)
    hanoi(n - 1, process, end, start)
N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3, 2)
