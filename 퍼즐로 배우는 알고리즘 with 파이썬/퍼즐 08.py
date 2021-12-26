# 8-1: 첫시도
    # 탐욕법: 싫어하는 관계가 가장 적은 친구부터 선택함. 즉, 연결된 변의 수가 가장 작은 꼭짓점을 선택.


# 8-2: 항상 가장 많은 경우 선택하기
    # 1. 싫어하는 관계를 우선은 생각하지 말고, 저녁 파티에 초대할 수 있는 친구들의 가능한 모든 조합을 생성합니다.
    # 2. 각 조합에 싫어하는 관계에 있는 친구들이 같이 들어있는지 확인하고, 그렇다면 해당 조합을 제거합니다.
    # 3. 남아있는 가능한 조합들 중 가장 많은 사람이 포함된 조합을 찾습니다. 이것이 바로 최선의 결과입니다. 여기에는 같은 수의 친구들을 가진 여러 조합이 있을 수 있습니다.


# 8-3: 모든 조합 생성하기
def Combinations(n, guestList): # 5, ['A', 'B', 'C', 'D', 'E']
    allCombL = [] # []
    for i in range(2**n): # 2**n번 반복문 실행
        num = i # 0 1
        cList = [] # []
        for j in range(n): # n번 반복문 실행 
            if num % 2 == 1: # x x x x x o
                cList = [guestList[n - 1 - j]] + cList # [guestList[5 - 1 - 0]]
            num = num // 2 # 0
        allCombL.append(cList) # allCombL = []
    return allCombL

# all_Comb = Combinations(5, ['A', 'B', 'C', 'D', 'E'])
# print(all_Comb)


# 8-4: 친하지 않는 조합 제거하기
def removeBadCombinations(allCombL, dislikePairs):
    allGoodCombinations = []
    for i in allCombL:
        good = True
        for j in dislikePairs: # 싫어하는 사람들의 리스트를 빼내는 반복문
            if j[0] in i and j[1] in i:
                good = False
        if good:
                allGoodCombinations.append(i)
    return allGoodCombinations
# dislike_Comb = removeBadCombinations(all_Comb, [['A', 'B'], ['B', 'E']])
# print(dislike_Comb)


# 8-5: 최대 조합 고르기
def InviteDinner(guestList, disLikePairs):
    allCombL = Combinations(len(guestList), guestList) # 위에 함수를 출력한 것.
    allGoodCombinations = removeBadCombinations(allCombL, disLikePairs) # 위에 함수를 출력한 것.
    invite = []
    for i in allGoodCombinations: 
        if len(i) > len(invite): # 전에 실행됐던 반복문의 i보다 리스트가 길면 i
            invite =  i
    print('Optimum Solution:', invite)
    
max_Comb: InviteDinner(['A', 'B', 'C', 'D', 'E'], [['A', 'B'], ['B', 'E']])


# 8-6: 메모리 사용량 최적화하기
def InviteDinnerOptimized(guestList, dislikePairs):
    n, invite = len(guestList), []
    for i in range(2**n):
        Combination = []
        num = i
        for j in range(n): # 6-9번째 줄에서 num = i 에 해당하는 조합을 생성
            if (num % 2 == 1):
                Combination = [guestList[n - 1 - j]] + Combination
            num = num // 2
        good = True # 10 - 13번째 줄에서 이 조합이 좋은지 나쁜지를 결정
        for j in dislikePairs:
            if j[0] in Combination and j[1] in Combination:
                good = False
        if good: # 14 - 16번째 줄에서 만약 현재 조합이 더 많은 친구들을 포함하고 있다면, 지금까지의 최선의 결과를 갱신함.
            if len(Combination) > len(invite):
                invite = Combination
    print('Optimum Solution:', invite)

InviteDinnerOptimized(['A', 'B', 'C', 'D', 'E'], [['A', 'B'], ['B', 'E']])
                
                      
# 연습문제
                      
print(0.1 + 0.2)

                      
            