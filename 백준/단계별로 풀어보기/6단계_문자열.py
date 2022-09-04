# 11654: 아스키 코드
A = input()
print(ord(A))


# 11720: 숫자의 합
N = int(input())
num = int(input())
answer = 0
for i in str(num):
    answer += int(i)
print(answer)


# 10809: 알파벳 찾기
S = input() # 문자열 입력받기
A = "abcdefghijklmnopqrstuvwxyz" # 알파벳
A_list = "" # 빈 문자열
for i in A: # 알파벳을 하나씩 넣어서 확인
    if i in S: # 입력받은 문자열 안에 알파벳이 있으면
        A_list += str(S.index(i)) + " " # 빈 문자열에 공백을 뒤에 넣고 추가
    else: # 없으면
        A_list += "-1 " # 공백을 -1뒤에 넣고 추가
print(A_list)


# 2675: 문자열 반복
T = int(input())
S_result = [] # 결과를 한 번에 출력해 주기위해 빈 리스트를 만듦
for i in range(T): # 테스트 케이스 반복
    R, S = map(str, input().split(" ")) # 입력받기
    P = "" # P를 빈 문자열로 시작해 하나씩 넣기 위해 만듦
    for x in range(len(S)): # S의 길이만큼 반복
        P += S[x] * int(R) # S의 각 문자들을 R과 곱해 P를 만들어줌
    S_result += [P] # 결과에 리스트로 추가
for j in S_result: # 반복문을 이용해 한 번에 출력
    print(j)


# 1157: 단어 공부
from collections import Counter # 최빈값을 구하는 모듈. max() 함수로 최빈값을 구할 수 있지만 최빈값이 2개 이상일때는 안됨.
string = input() # 문자열 입력받기
string = string.lower() # 문자열을 소문자로 변경
string_count = Counter(string) # 딕셔너리 형태로 입력받은 문자열의 각각의 빈도수를 나오게 함
string_count = string_count.most_common() # 내림차순으로 튜플 형태로 나타내줌
if len(string_count) == 1: # 문자열을 1개만 입력받았을 때 이렇게 구분을 안해주면 인덱스 에러가 남
    print(string_count[0][0].upper()) # 인덱싱 후 대문자로 출력
else:
    if string_count[0][1] == string_count[1][1]: # string_count는 리스트 안에 내림차순으로 튜플형태로 정렬된 것이기 때문에 인덱싱으로 확인
        print("?") # 최빈값이 2개 이상일때에는 물음표 출력
    else:
        print(string_count[0][0].upper()) # 최빈값이 1개일 때에는 string_count의 첫 번째 문자를 바로 출력해주면 됨


# 1152: 단어의 개수
string = input()
string_split = string.split(" ") # 공백 기준으로 잘라서 리스트로 넣음
if string_split[0] == "":
    del string_split[string_split.index("")]
    if string_split[-1] == "": # 앞뒤가 모두 공백인 경우 때문에 여기까지 해줘야 함
        del string_split[string_split.index("")]
elif string_split[-1] == "":
    del string_split[string_split.index("")]
    if string_split[0] == "": # 앞뒤가 모두 공백인 경우 때문에 여기까지 해줘야 함
        del string_split[string_split.index("")]
print(len(string_split))


# 2908: 상수
a, b = map(int, input().split(" "))
a = str(a)
a_new = "{}{}{}".format(a[-1], a[-2], a[-3])
b = str(b)
b_new = "{}{}{}".format(b[-1], b[-2], b[-3])
print(max(int(a_new), int(b_new)))


# 5622: 다이얼
string = input()
time_result = 0
for i in string:
    if i == "A" or i == "B" or i == "C":
        time_result += 3
    elif i == "D" or i == "E" or i == "F":
        time_result += 4
    elif i == "G" or i == "H" or i == "I":
        time_result += 5
    elif i == "J" or i == "K" or i == "L":
        time_result += 6
    elif i == "M" or i == "N" or i == "O":
        time_result += 7
    elif i == "P" or i == "Q" or i == "R" or i == "S":
        time_result += 8
    elif i == "T" or i == "U" or i == "V":
        time_result += 9
    elif i == "W" or i == "X" or i == "Y" or i == "Z":
        time_result += 10
print(time_result)
        

# 2941: 크로아티아 알파벳
string = input() # 입력받기
cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="] # 크로아티아 알파벳들을 리스트에 넣어줌
for i in cro: # 크로아티아 알파벳을 하나씩 넣음
    if i in string: # 입력받은 값 안에 크로아티아 알파벳이 존재하면
        string = string.replace(i, str(1)) # 그 자리를 1로 바꿈
print(len(string)) # 최종 문자열의 길이를 세주면 답


# 1316: 그룹 단어 체커
N = int(input())
group_word = 0
for _ in range(N):
    word = input()
    error = 0
    for index in range(len(word) - 1): # 인덱스 범위 생성: 0부터 단어개수 -1까지
        if word[index] != word[index + 1]: # 연속하는 두 문자가 다를 때
            new_word = word[index + 1:] # 현재 글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0: # 남은 문자열에서 현재 글자가 있다면
                error += 1 # error에 1씩 증가
    if error == 0:
        group_word += 1 # error가 0이면 그룹단어
print(group_word)
        

        
      

            


            

    
    




    


