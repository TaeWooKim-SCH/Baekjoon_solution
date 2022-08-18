# 2750: 수 정렬하기
for i in sorted([int(input()) for _ in range(int(input()))]):
    print(i)



# 2751: 수 정렬하기 2
import sys 
N = int(sys.stdin.readline())
nums = set() # 중복되지 않아야 하기 때문에 집합을 이용함
for _ in range(N):
    nums.update({int(sys.stdin.readline())})
nums = sorted(nums)
for i in nums:
    print(i)



# 10989: 수 정렬하기 3
def counting_sort(n):
    # n: 수의 개수
    counting_array = [0 for _ in range(10001)] # 수의 최대값 만큼 배열을 만들어줌
    for i in range(n): # 수의 개수만큼 반복
        num = int(sys.stdin.readline()) # 수 입력받기
        counting_array[num] += 1 # 즉시 배열에 카운팅하기
    for x in range(10001): # 수의 개수만큼 반복
        if counting_array[x] != 0: # 카운팅이 0개인 것은 고려할 필요가 없음
            for j in range(counting_array[x]): # 각 수의 개수만큼 반복
                print(x) # 배열의 인덱스 번호 출력
                counting_array[x] -= 1 # 0을 만들어주기 위해 출력할때마다 1을 빼줌
import sys
N = int(sys.stdin.readline())
counting_sort(N)



# 25305: 커트라인
N, k = map(int, input().split())
x_list = sorted(list(map(int, input().split())))
print(x_list[-k])



# 2108: 통계학
def statistics(n):
    # 변수 설정
    average = 0 # 산술평균
    median = n // 2 + 1 # n은 홀수이기 때문에 중앙값이 2로 나눈 후 1을 더한 수 번째 있는 값임
    median_end = 0 # 최종 중앙값
    mode = 0 # 최빈값
    range_min = 0 # 범위
    range_max = 0 # 범위

    # 배열을 만들어주기 위한 코드
    n_array = [0 for _ in range(-4000, 4001)]
    for _ in range(n):
        num = int(sys.stdin.readline())
        n_array[num] += 1

    # 통계값 계산하기
    for i in range(-4000, 4001):
        if n_array[i] != 0:
        # 산술평균을 위한 코드
            average += (n_array[i] * i)
        # 중앙값을 위한 코드
            median -= n_array[i]
            if median <= 0:
                median = n # n2_end가 계속 업데이트 되기 때문에 양수로 n2를 양수로 바꿔줌
                median_end = i
        # 범위를 위한 코드
            range_max = i # 최댓값은 그냥 최종값을 넣으면 됨
    for x in range(-4000, 4001):
        if n_array[x] != 0:
            range_min = x # 최솟값은 바로 첫 번째에 들어오는 수를 넣으면 됨
            break # 바로 중단
        # 최빈값을 위한 코드
    mode = max(n_array)
    mode_list = []
    for k in range(-4000, 4001):
        if n_array[k] == mode:
            mode_list.append(k)
    if len(mode_list) >= 2:
        mode = sorted(mode_list)[1]
    else:
        mode = mode_list[0]

    # 출력
    print(round(average / n))
    print(median_end)
    print(mode)
    print(range_max - range_min)
import sys
N = int(sys.stdin.readline())
statistics(N)



# 1427: 소트인사이드
def sortinside(n):
    n_list = []
    n_str = ''
    for i in str(n):
        n_list.append(i)
    for x in reversed(sorted(n_list)):
        n_str += x
    print(n_str)
sortinside(int(input()))



# 11650: 좌표 정렬하기
def location_array(n):
    loc_list = []
    for _ in range(n):
        loc_list.append(list(map(int, input().split(" "))))
    for p, q in sorted(loc_list):
        print(p, q)
N = int(input())
location_array(N)



# 11651: 좌표 정렬하기 2
def location_array(n):
    loc_list = []
    for _ in range(n):
        loc_list.append(list(map(int, input().split(" "))))
    for p, q in sorted(sorted(loc_list), key = lambda x: x[1]):
        print(p, q)
N = int(input())
location_array(N)



# 1181: 단어 정렬
def as_array(n):
    array = set()
    for _ in range(n):
        array.update({input()})
    for i in sorted(sorted(array), key = lambda x: len(x)):
        print(i)
as_array(int(input()))



# 10814: 나이순 정렬
def old_array(n):
    old_list = [list(map(str, input().split(" "))) for _ in range(n)]
    for x, y in sorted(old_list, key = lambda x: int(x[0])):
        print(x, y)
old_array(int(input()))



# 18870: 좌표 압축
 # 시간초과
import sys
def loc_press(n):
    loc_list = list(map(int, sys.stdin.readline().split(" "))) # 리스트로 넣어줌
    loc_sorted = sorted(set(loc_list)) # 중복된 숫자들을 제거하고 오름차순 정렬
    for i in range(n):
        for x in loc_sorted:
            if loc_list[i] == x: # 만약 인덱싱한 값과 오름차순 정렬한 값들 중 같은 것이 있다면
                loc_list[i] = loc_sorted.index(x) # 정렬한 값의 인덱스 값으로 바꿔줌
    # 출력
    for j in loc_list:
        print(j, end = " ")
N = int(sys.stdin.readline())
loc_press(N)

 # 성공: 딕셔너리로 접근
import sys
def loc_press(n):
    loc_list = list(map(int, sys.stdin.readline().split(" "))) # 리스트로 넣어줌
    loc_sorted = sorted(set(loc_list)) # 중복된 숫자들을 제거하고 오름차순 정렬
    loc_dic = {loc_sorted[x]: x for x in range(len(loc_sorted))} # 딕셔너리에 각 키 값과 밸류 값을 넣어줌
    for i in loc_list: 
        print(loc_dic[i], end = ' ')
N = int(sys.stdin.readline())
loc_press(N)

