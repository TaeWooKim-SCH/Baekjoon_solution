# 15596: 정수 N개의 합
def solve(a):
    return sum(a)


# 4673: 셀프 넘버
self_num = set(range(1, 10001)) # 1부터 10000까지 숫자. 나중에 여기서 생성자를 뺄 거임
num = set() # 집합화
for i in self_num: # 1부터 10000까지 숫자를 넣음
    for x in str(i): # 각각의 숫자를 문자열로 바꾼 후 각 자리의 숫자를 집어 넣음
        i += int(x) # 각 자리의 숫자들을 i와 더함
    num.add(i) # 생성자들을 num에 넣음
num = set(num) # num을 집합화
self_num = sorted(self_num - num) # 1부터 10000까지 숫자에서 생성자들을 제거하면 셀프넘버만 남음. 그 후 순서대로 정렬
for j in self_num: # 반복문을 사용해 한줄씩 출력
    print(j)


# 1065: 한수
N = int(input()) # N 입력받기
hansu = set() # 한수를 공집합으로 생성
for i in range(1, N + 1): # 입력받은 N까지 숫자를 다 넣음
    if len(str(i)) == 1: # 숫자를 문자열로 바꿔서 자리수가 1개인지 확인
        hansu.add(i) # 자리수가 1개인 모든 숫자는 한수임
    elif len(str(i)) == 2:
        hansu.add(i) # 자리수가 2개인 모든 숫자는 한수임
    elif len(str(i)) == 3: # 자리수가 3개부터는 각각 확인을 해줘야 하는데 이 문제에선 1000보다 작거나 같은 수만 입력받기 때문에 3자리까지만 확인하면 됨
        if (int(str(i)[0]) - int(str(i)[1])) == (int(str(i)[1]) - int(str(i)[2])):
            hansu.add(i)
print(len(hansu))
