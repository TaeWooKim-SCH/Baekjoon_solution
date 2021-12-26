Talents = ['Sing', 'Dance', 'Magic', 'Act', 'Flex', 'Code']
Candidates = ['Aly', 'Bob', 'Cal', 'Don', 'Eve', 'Fay']
CandidateTalents = [['Flex', 'Code'], ['Dance', 'Magic'], ['Sing', 'Magic'], ['Sing', 'Dance'], ['Dance', 'Act', 'Code'], ['Act', 'Code']]


# 9-1: 조합 하나씩 만들고 테스트하기
def Hire4Show(candList, candTalents, talentList):
    n = len(candList)
    hire = candList[:]
    for i in range(2 ** n):
        Combination = []
        # print("Combination:", Combination)
        num = i
        for j in range(n):
            if (num % 2 == 1):
                Combination = [candList[n - 1 - j]] + Combination
                # print("Combination:", Combination)
            num = num // 2
            # print("num:", num)
        if Good(Combination, candList, candTalents, talentList):
            if len(hire) > len(Combination):
                hire = Combination
    print('Optimum Solution:', hire)


# 9-2: 재능이 모자란 조합 결정하기

